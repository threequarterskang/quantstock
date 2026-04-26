from factor.base import Factor

class RSIFactor(Factor):
    def __init__(self, symbol, window=14):
        super().__init__(name=f"rsi_{symbol}")
        self.symbol = symbol
        self.window = 14

    def compute(self, df):
        
        close = df[self.symbol]["close"]
        delta = close.diff()

        gain = delta.clip(lower=0).rolling(self.window).mean()
        loss = (-delta.clip(upper=0)).rolling(self.window).mean()

        rs = gain / loss
        rsi = 100 - (100 / (1+rs))

        return rsi
    
    def params(self):
        return {
            "symbol": self.symbol,
            "window": self.window
        }
