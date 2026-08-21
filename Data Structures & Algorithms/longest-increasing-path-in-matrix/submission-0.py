class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = {}
        direct = [(1,0), (-1,0), (0,1), (0,-1)]
        ans = 0
        def dfs(i,j,visit):
            if (i,j) in dp:
                return dp[(i,j)]
            
            max_path = 0
            for dy, dx in direct:
                new_i, new_j = i + dy, j + dx
                if ((new_i, new_j) not in visit and 0 <= new_i < m and 0 <= new_j < n
                    and matrix[new_i][new_j] > matrix[i][j]):                   
                    visit.add((new_i,new_j))
                    path = 1 + dfs(new_i,new_j,visit)
                    visit.remove((new_i,new_j))
                    max_path = max(max_path, path)
            dp[(i,j)] = max_path
            return dp[(i,j)]
        
        for i in range(m):
            for j in range(n):
                visit = set()
                res = 1 + dfs(i,j,visit)
                ans = max(ans,res)
        return ans
