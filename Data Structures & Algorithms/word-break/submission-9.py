class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True

        for i in range(n-1,-1,-1):
            for w in wordDict:
                wordLen = len(w)
                if i + wordLen <= n and s[i:i+wordLen] == w:
                    if dp[i + wordLen]:
                        dp[i] = True
                        continue
        return dp[0]