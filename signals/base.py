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
                -1 short
        """
        raise NotImplementedError
    
    def params(self):
        return {}