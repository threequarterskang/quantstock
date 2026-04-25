import yfinance as yf
import pandas as pd

def getdata(symbol, interval, period):
    df = yf.download(symbol, interval=interval, period=period)

    df = df.dropna()
    
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df.columns = [c.lower() for c in df.columns]

    return df

def save_parquet(df, path):
    df.to_parquet(path)

def load_parquet(path):
    return pd.read_parquet(path)
