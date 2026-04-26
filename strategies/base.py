class Strategies:

    def __init__(self, name=None):
        self.name = name

    def generate(self, df):
        """
        这个系统输出：
        t1: 1.0 满仓
        t2: 0.5 减半仓
        t3: -1  清仓

        output
            pd.series
                +1 -> long
                0 ->  neutral
                -1 -> short       
        """
        raise NotImplementedError
    
    def params(self):
        return {}

