import pandas as pd

# 数据对齐，避免日期不一致
class DataAligner:

    def __init__(self, fill_method="backtest"):
        """
        fill mode :
            - backtest: 历史数据对齐 DataFrame
            - live: 实时数据(Snapshot)
        """
        # 对齐方式
        self.method = fill_method

        # live mode 
        self.latest = {}

        # backtest mode
        self._backtest_df = None    # 存历史数据
        self._backtest_index =None  # 控制回测进度
        self._i = 1 # 当前回测执行到第几根k线

    # backtest专用对齐,不需要return，只需改变self的两个属性值
    def align(self, data_dict):
        """
        df_list = {
            "QQQ": df1
            "VXN": df2
        }
        """
        df_list = []
        common_index = None # 股票共同时间轴

        # 遍历列表处理
        for name, d in data_dict.items():
            """
            先初始化index,然后与后面的每个数据共同相交,计算出相同的交集index
            """
            if common_index == None:
                common_index = d.index
            else:
                common_index = common_index.intersection(d.index)

            # 防止修改原始输入数据
            d = d.copy()

            """
            原来的
            open high low close
            现在的
            (QQQ, open) (QQQ, high) (QQQ, low) (QQQ, close)
            """
            d.columns = pd.MultiIndex.from_product([[name], d.columns])
            # 收集每个资产
            df_list.append(d)

        # 严格对齐时间轴
        df_list = [d.reindex(common_index) for d in df_list]

        # 按时间拼接横向数据
        df = pd.concat(df_list, axis=1).sort_index()

        # 防止未来函数 例如 10:01只能看到10:00时的数据，看不到10:01的数据
        df = df.shift(1)

        self._backtest_df = df
        self._backtest_index = df.index

    # backtest的流式输出
    def next(self):
        """
        每次返回一个snapshot(模拟实盘)
        """

        if self.method != "backtest":
            raise ValueError("not in backtest mode")

        if self._i >= len(self._backtest_index):
            return None

        row = self._backtest_df.iloc[self._i]

        self._i += 1

        return self._to_snapshot(row)


    # 统一snapshot转换器
    def _to_snapshot(self, row):
        """
        backtest row ---> snapshot dict
        """

        snapshot = {}

        for (symbol, field), value in row.items():
            if symbol not in snapshot:
                snapshot[symbol] = {}
            snapshot[symbol][field] = value
        
        return snapshot


    # Live 更新数据
    def update(self, symbol, data):
        """
        实盘推送数据
        data: dict or series
        """

        self.latest[symbol] = data

    # Live snapshot 输出
    def snapshot(self):
        """
        当前市场状态(实盘)
        """
        if self.method != "live":
            raise ValueError("not in live mode")
        
        return self.latest


"""
backtest usage:
aligner = DataAligner(method="backtest")

aligner.set_backtest_data(data_dict)

while True:
    snapshot = aligner.next()

    if snapshot is None:
        break

    signal = strategy.on_data(snapshot)

live usage:
aligner = DataAligner(method="live")

aligner.update("AAPL", {"close": 190})
aligner.update("QQQ", {"close": 410})

snapshot = aligner.snapshot()

signal = strategy.on_data(snapshot)
"""