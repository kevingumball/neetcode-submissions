class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        minHeap = [(grid[0][0], 0, 0)]
        res = 0
        visit = set()
        visit.add((0,0))

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == n - 1 and c == n - 1:
                return t
            
            for dr, dc in directions:
                newr, newc = r + dr, c + dc
                if (newr < 0 or newc < 0 or newr == n or newc == n or (newr, newc) in visit):
                    continue
                heapq.heappush(minHeap, (max(t,grid[newr][newc]), newr, newc))
                visit.add((newr, newc))
            
        