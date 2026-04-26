class Signal:

    def __init__(self, name=None):
        self.name = name
    
    def generate(self, factor):
        """
        input:
            factors: dict[str, pd.Series]

        output:
            pd.series (signal)
                +1 long
                0   netural
                -1 shorta

                    rsi   macd
        t1           -1     0
        t2            0     1
        t3            1    -1
        """
        raise NotImplementedError
    
    def params(self):
        return {}