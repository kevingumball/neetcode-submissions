class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r, c, t):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit or grid[r][c] > t):
                return False
            if r == ROWS - 1 and c == COLS - 1:
                return True
            
            visit.add((r,c))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, t):
                    return True
        
        t = -1
        while True:
            t += 1
            visit =set()
            if dfs(0, 0, t):
                return t
        

        