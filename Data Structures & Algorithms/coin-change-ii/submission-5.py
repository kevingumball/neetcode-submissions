class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = {}

        def dfs(i, cur):
            if cur == amount:
                return 1
            if i == len(coins):
                return 0
            if (i, cur) in dp:
                return dp[(i,cur)]

            res = 0
            if amount - cur >= coins[i]:
                res += dfs(i + 1, cur)
                res += dfs(i, cur + coins[i])
            dp[(i,cur)] = res
            return res

        return dfs(0,0)