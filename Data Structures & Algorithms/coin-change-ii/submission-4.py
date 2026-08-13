class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        coins.sort()
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(n-1, -1, -1):
            new_dp = [0] * (amount + 1)
            new_dp[0] = 1
            for a in range(1, amount + 1):
                new_dp[a] = dp[a]
                if a >= coins[i]:
                    new_dp[a] += new_dp[a - coins[i]]
            dp = new_dp
        return dp[amount]