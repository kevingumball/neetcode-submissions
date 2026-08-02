class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True

        for i in range(n-1,-1,-1):
            for word in wordDict:
                wordLen = len(word)
                if i + wordLen <= n and s[i:i + wordLen] == word:
                    if dp[i + wordLen]:
                        dp[i] = True
        return dp[0]
                
