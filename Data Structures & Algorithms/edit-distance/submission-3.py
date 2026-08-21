class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = {}

        def dfs(i,j):
            if j == n:
                if i == m:
                    return 0
                return m - i
            if i == m:
                return n - j

            if (i,j) in dp:
                return dp[(i,j)]
            res = float("inf")
            if i < m and word1[i] == word2[j]:
                res = min(res,dfs(i+1,j+1))
            res = min(res,1 + dfs(i,j+1))
            res = min(res,1 + dfs(i+1,j))
            res = min(res,1 + dfs(i+1,j+1))
            dp[(i,j)] = res
            return res
        return dfs(0,0)



