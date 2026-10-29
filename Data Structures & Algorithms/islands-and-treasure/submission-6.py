class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def addnum(r,c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visit or grid[r][c] == -1):
                return
            else:
                q.append((r,c))
                visit.add((r,c))

        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        cur = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = cur
                addnum(r+1,c)
                addnum(r-1,c)
                addnum(r,c+1)
                addnum(r,c-1)
            cur += 1
        
        


        