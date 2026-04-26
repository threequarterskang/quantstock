from strategies.base import Strategies
import pandas as pd

class MutilFactorStrategy(Strategies):

    def __init__(self, weights=None):
        super().__init__(name="multi_factor")

    def generate(self, df):
        # 创建一个和df完全对齐的时间序列，但值为0
        result = pd.Series(0, index=df.index)

        for name in df.columns:
            # 如果没有定义weight，就取1.0
            w = self.weights.get(name, 1.0)

            # 结果等于df[name]的值乘以权重
            result += df[name] * w
        
        # 将结果限制在-1到1之间，大于1就取1，小于-1就取-1
        return result.clip(-1,1)
    
    def params(self):
        return {
            "weights": self.weights
        }
    

