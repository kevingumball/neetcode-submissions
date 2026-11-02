class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            cur = 0

            while q:
                row, col = q.popleft()
                cur += 1
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == 0):
                        continue
                    else:
                        grid[nr][nc] = 0
                        q.append((nr,nc))
            return cur
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, bfs(r,c))
        return res
        