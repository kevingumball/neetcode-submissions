class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {n:1}

        for i in range(n-1,-1,-1):
            if s[i] == '0':
                dp[i] = 0
                continue
            res = dp[i+1]
            if i + 1 < n and (s[i] == '1' or s[i] == '2' and s[i+1] < '7'):
                res += dp[i+2]
            dp[i] = res
        return dp[0]
