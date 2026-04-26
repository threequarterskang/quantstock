class Pipeline:

    def __init__(self, factors, signals):
        self.factors = factors
        self.signals = signals

    def run(self, df):
        """ 
        从factor那里获取数据
        然后保存成
        {
            "rsi_qqq": Series,
            "macd_qqq": Series
        }
        """
        factor_outputs = {}
        for name, f in self.factors.items():
            factor_outputs[name] = f.coumpute(df)
        """
        {
           "rsi_qqq": Series,
            "macd_qqq": Series
        }
        """
        signal_outputs = {}
        for name, s in self.signals.items():
            signal_outputs[name] = s.generate(factor_outputs)

        return factor_outputs, signal_outputs


        