class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = 0
        minheap = [(grid[0][0], 0, 0)]
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visit = set()

        while minheap:
            hei, r, c = heapq.heappop(minheap)
            if (r,c) in visit:
                continue
            res = max(res, hei)
            if r == len(grid) - 1 and c == len(grid) - 1:
                return res
            visit.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid) or (nr, nc) in visit):
                    continue
                heapq.heappush(minheap, (grid[nr][nc], nr, nc))
        
            
        