class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(t), len(s)
        dp = [[0]*(m+1) for _ in range(n + 1)]
        for j in range(m+1):
            dp[n][j] = 1
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                dp[i][j] = dp[i][j+1]
                if t[i] == s[j]:
                    dp[i][j] += dp[i+1][j+1]
        return dp[0][0]



