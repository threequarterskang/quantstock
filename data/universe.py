class Universe:

    def __init__(self, config=None):
        
        default = {
            "equity": ["QQQ", "SPY"],
            "macro": ["^VXN"],
            "crypto": ["BTC-USD"]
        }

        self.config = default or config

    # 默认获取所有资产
    def get_all(self):
        return (
            self.config["equity"] +
            self.config["macro"] +
            self.config["crypto"]
        )
    
    def filter(self, asset_type="all"):
        if asset_type == "equity":
            return self.config["equity"]
        elif asset_type == "macro":
            return self.config["macro"]
        elif asset_type == "crypto":
            return self.config["crypto"]
        else:
            return self.get_all()