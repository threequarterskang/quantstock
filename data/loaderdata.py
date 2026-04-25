import yfinance as yf
import pandas as pd

# 获取文件：symbol=名称 interval=区间 period=周期
def getdata(symbol, interval, period):
    df = yf.download(symbol, interval=interval, period=period)

    # 去除N/A数值
    df = df.dropna

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    
    # 将列名调成小写
    df.columns = [c.lower() for c in df.columns]

    return df