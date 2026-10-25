class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        n = len(word)
        path = set()
        def dfs(r, c, i):
            if i >= n:
                return True
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r,c) in path or board[r][c] != word[i]):
                return False
            path.add((r,c))
            top = dfs(r-1,c,i+1)
            bottom = dfs(r+1,c,i+1)
            left = dfs(r,c-1,i+1)
            right = dfs(r,c+1,i+1)
            path.remove((r,c))
            return top or bottom or left or right

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
        