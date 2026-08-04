class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0:0}

        for i in range(1,amount + 1):
            res = float("inf")

            for c in coins:
                if i - c >= 0:
                    res = min(res, 1 + dp[i - c])
            dp[i] = res
        
        return dp[amount] if dp[amount] != float("inf") else -1