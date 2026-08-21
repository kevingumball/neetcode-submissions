class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(t), len(s)
        dp = {}

        def dfs(i,j):
            if i == n:
                return 1
            if j == m:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]     
            res = 0      
            if t[i] == s[j]:
                res = dfs(i+1, j+1)
            res += dfs(i, j + 1)  
            dp[(i,j)] = res
            
            return res
        return dfs(0,0)

