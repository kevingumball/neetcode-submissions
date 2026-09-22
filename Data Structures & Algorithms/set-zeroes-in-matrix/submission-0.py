class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        rw, cl = [-1] * ROWS, [-1] * COLS

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    rw[i] = 0
                    cl[j] = 0
        
        for i, num in enumerate(rw):
            if num == 0:
                for j in range(COLS):
                    matrix[i][j] = 0
        
        for j, num in enumerate(cl):
            if num == 0:
                for i in range(ROWS):
                    matrix[i][j] = 0
        
        