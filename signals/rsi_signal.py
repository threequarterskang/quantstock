from signals.base import Signal

class RSISignal(Signal):
    def __init__(self, factor_name, low=30, high=70):
        super().__init__(name=f"{factor_name}_signal")
        self.factor_name = factor_name
        self.low = low
        self.high = high

    def generate(self, factors):
        
        rsi = factors[self.factor_name]

        # 复制避免修改原数据
        signal = rsi.copy()

        # dict里的值保持中性，保持形状和清空数值
        signal[:] = 0

        # 使用了pandas的特性，而不用调用pandas，因为以前的函数已经用了pandas来生成这个对象了
        signal[rsi < self.low] = 1
        signal[rsi > self.high] = -1

        return signal
    
    def params(self):
        return {
            "low": self.low,
            "high": self.high
        }
        