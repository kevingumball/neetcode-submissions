class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {(m-1,n-1) : 1}

        def dfs(i,j):
            if i >= m or j >= n:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            
            dp[(i,j)] = dfs(i+1,j) + dfs(i,j+1)
            return dp[(i,j)]
        return dfs(0,0)