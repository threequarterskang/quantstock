class Factor:

    def __init__(self, name=None):
        self.name = name
    
    # 每个策略都需要有这个函数
    def compute(self, df):
        """
        input:
            df: MultiIndex DataFrame

        output:
            pd.Series (aligned index)
        """
        raise NotImplementedError
    
    # 可以调用此函数来获取当前factor的参数
    def params(self):
        return {}
    