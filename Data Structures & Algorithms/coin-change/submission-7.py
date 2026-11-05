class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            res = float("inf")
            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + dfs(amount - c))
            memo[amount] = res
            return memo[amount]
        ans = dfs(amount)
        return ans if ans < float("inf") else -1
        