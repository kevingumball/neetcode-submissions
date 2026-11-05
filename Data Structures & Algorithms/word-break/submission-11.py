class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = {}
        def dfs(i):
            if i == n:
                return True
            if i in dp:
                return dp[i]
            for word in wordDict:
                wlen = len(word)
                if (n - i) - wlen >= 0 and s[i:i+wlen] == word:
                    if dfs(i + wlen):
                        return True
            dp[i] = False   
            return False
        return dfs(0)

        