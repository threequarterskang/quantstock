import pandas as pd
import numpy as np

class Allocator:

    def __init__(self):
        pass

    def allocate(self, signals):
        """
        signals: dict[str, pd.Series]
        return: pd.DataFrame
        """
        