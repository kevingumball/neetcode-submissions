class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, canbuy):
            if i >= len(prices):
                return 0
            if (i, canbuy) in dp:
                return dp[(i, canbuy)]
            
            cooldown = dfs(i+1, canbuy)
            if canbuy:
                buy = dfs(i+1, not canbuy) - prices[i]
                dp[(i, canbuy)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not canbuy) + prices[i]
                dp[(i, canbuy)] = max(sell, cooldown)
            return dp[(i, canbuy)]

        return dfs(0, True)