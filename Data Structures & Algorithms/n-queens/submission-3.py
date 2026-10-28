class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        colset = set()
        pos = set()
        neg = set()
        res = []


        def dfs(r):
            if r >= n:
                cur = board.copy()
                cur = ["".join(row) for row in cur]
                res.append(cur)
                return
            
            for c in range(n):
                if (c in colset or (r + c) in pos or (r - c) in neg):
                    continue
                colset.add(c)
                pos.add(r+c)
                neg.add(r-c)
                board[r][c] = "Q"

                dfs(r + 1)

                colset.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
                board[r][c] = "."
        
        dfs(0)
        return res


                
        