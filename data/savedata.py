import pandas as pd

# 保存文件 path=“/path/filename”
def save_parquet(df, path):
    df.to_parquet(path)

# 加载文件 path=“/path/filename”
def load_parquet(path):
    return pd.read_parquet(path)