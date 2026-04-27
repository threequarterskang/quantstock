class Universe:

    def __init__(self, config=None, roles=None):
        
        # 资产分类
        default = {
            "equity": ["QQQ", "SPY"],
            "macro": ["^VXN"],
            "crypto": ["BTC-USD"]
        }

        self.config = config or default

        # 每种资产类别的角色
        default_role = {
            "trade": ["QQQ"],
            "filter": ["SPY"],
            "risk": ["^VXN"]
        }

        self.roles = roles or default_role

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
        

    def get_by_role(self, role_type="all"):
        