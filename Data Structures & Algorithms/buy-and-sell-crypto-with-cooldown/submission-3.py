class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        n = len(prices)

        def dfs(i, profit, canbuy):
            if i >= n:
                return profit
            if (i, profit, canbuy) in dp:
                return dp[(i, profit, canbuy)]
            
            cooldown = dfs(i+1, profit, canbuy)

            if canbuy:
                buy = dfs(i+1, profit - prices[i], not canbuy)
                dp[(i, profit, canbuy)] = max(buy, cooldown)
                return dp[(i, profit, canbuy)]
            else:
                sell = dfs(i+2, profit + prices[i], not canbuy)
                dp[(i, profit, canbuy)] = max(sell, cooldown)
                return dp[(i, profit, canbuy)]

        return dfs(0,0,True)