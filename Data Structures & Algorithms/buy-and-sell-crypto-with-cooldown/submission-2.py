class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buying: i+1  we have cooldown option  
        #selling: i+2 we have cooldown option all the time

        dp = {}

        def dfs(i, can_buy):
            if i >= len(prices):
                return 0
            if (i, can_buy) in dp:
                return dp[(i, can_buy)]
            if can_buy:
                # 手里没股票
                # 今天买入，明天就不能买了
                buy = -prices[i] + dfs(i + 1, False)
                # 今天不买，明天仍然可以买
                skip = dfs(i + 1, True)

                dp[(i, can_buy)] = max(buy, skip)

            else:
                # 手里有股票

                # 今天卖出，冷冻一天，所以去 i + 2
                sell = prices[i] + dfs(i + 2, True)
                # 今天不卖，继续持有，明天仍然不能买
                hold = dfs(i + 1, False)

                dp[(i, can_buy)] = max(sell, hold)

            return dp[(i, can_buy)]

        return dfs(0, True)