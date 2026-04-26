import pandas as pd

class SignalBuilder:

    def __init__(self):
        pass

    def build(self, signals):
        """
        input:
            signals: dict[str, pd.series]

        output:
        dataframe后
                    rsi_signal   macd_signal
        2024-01-01      1             0
        2024-01-02      0             1
        2024-01-03     -1            -1
        """

        df = pd.DataFrame(signals)

        df = df.fillna(0)

        return df