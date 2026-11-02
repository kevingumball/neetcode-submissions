class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        fresh = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        time = 0
        while q and fresh:
            time += 1
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != 1):
                        continue
                    else:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
        return time if fresh == 0 else -1

            
        