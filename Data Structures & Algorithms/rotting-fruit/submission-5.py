class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        rest = 0

        def addnum(r,c):
            nonlocal rest
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visit or grid[r][c] == 0):
                return
            else:
                q.append((r,c))
                visit.add((r,c))
                rest -= 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
                elif grid[r][c] == 1:
                    rest += 1
        time = 0
        while q and rest > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                addnum(r+1,c)
                addnum(r-1,c)
                addnum(r,c+1)
                addnum(r,c-1)
            time += 1

        return time if not rest else -1


        