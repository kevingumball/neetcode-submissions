class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        minheap = [(grid[0][0], 0, 0)]
        visit = set()
        res = 0

        while minheap:
            t, r, c = heapq.heappop(minheap)
            if (r,c) in visit:
                continue
            res = max(res, t)
            if r == ROWS - 1 and c == COLS - 1:
                return res
            visit.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visit):
                    continue
                heapq.heappush(minheap, (grid[nr][nc], nr, nc))
                
        
        

        