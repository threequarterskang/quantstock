class RiskManager:
    def __init__(self, rules):
        """
        规则列表
        """
        self.rules = rules

    def apply(self, weights, context):
        """
        weight来自portfolio的返回值
        context来自回测时数据,实盘会不同
        """
        for rule in self.rules:
            weights = rule.apply(weights, context)

        return weights
