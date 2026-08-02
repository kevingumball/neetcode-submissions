class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = {n:True}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            for word in wordDict:
                wl = len(word)
                if i + wl <= n and s[i:i+wl] == word:
                    if dfs(i + wl):
                        dp[i] = True
                        return True
            dp[i] = False
            return False

        return dfs(0)