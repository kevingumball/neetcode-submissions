class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        grid = [[-1] * len(text2) for _ in range(len(text1))]
        def dfs(i,j):
            if i >= m or j >= n:
                return 0
            if grid[i][j] != -1:
                return grid[i][j]
            
            if text1[i] == text2[j]:
                grid[i][j] = 1 + dfs(i+1,j+1)
                return grid[i][j]
            else:
                grid[i][j] = max(dfs(i+1,j) , dfs(i,j+1))
            return grid[i][j]
        return dfs(0,0)
