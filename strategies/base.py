class Strategies:

    def __init__(self, name=None):
        self.name = name

    def generate(self, signals):
        """
        input
            signals: dict[str, pd.series]

        output
            pd.series
                +1 -> long
                0 ->  neutral
                -1 -> short       
        """
        raise NotImplementedError
    
    def params(self):
        return {}

