class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = {n:True}

        def dfs(i):
            if i in dp:
                return dp[i]
            for w in wordDict:
                wordLen = len(w)
                if i + wordLen <= n and s[i : i + wordLen] == w:
                    if dfs(i + wordLen):
                        dp[i] = True
                        return True
                
            dp[i] = False
            return False
            
        return dfs(0)
        