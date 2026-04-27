import pandas as pd
import numpy as np

class BacktestEngine:
    
    def __init__(self,
                 initial_capital = 10000,   # 初始资产
                 commission = 0.0005,       # 手续费
                 slippage = 0.0005          # 滑点--市场流动性不足、市场剧烈波动、网络延迟或者下单时的价格变动
                 ):
        self.initial_capital = initial_capital
        self.commission = commission
        self.slippage = slippage

        self.equity = initial_capital
        self.positions = {}
        self.equity_curve = []
    
    # context builder
    def _build_context(self, pnl, returns, prices):
        return{
            "equity": self.equity,  # 资产
            "pnl": pnl,             # 账户盈亏金额 profit and loss
            "returns": returns,     # 收益率
            "prices": prices,       # 价格--资产的市场报价
            "position": self.positions  # 头寸和持仓
        }
    
    # execution simulation
    def _execution(self, prices, target_weights):
        pnl = 0 

        new_positions = {}

        

