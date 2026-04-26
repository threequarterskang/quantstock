import pandas as pd
import numpy as np

class Allocator:

    def __init__(self, leverage=1.0):
        # leverage为杠杆率
        self.leverage = leverage

    def allocate(self, signal):
        """
        input:
            signal: pd.series(-1,1)

        output:
            pd.series (weights)
        """
        # 复制signal数据，避免修改源数据
        weight = signal.copy()

        denom = weight.abs().sum()
        if denom != 0:
            weight = weight / denom
        
        weight = weight * self.leverage

        return weight




        