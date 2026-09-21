class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        layers = (min(ROWS, COLS) + 1) // 2
        res = []

        for y in range(layers):
            left = y
            top = y
            right = COLS - 1 - y
            bottom = ROWS - 1 - y

            # 只剩一列
            if top == bottom:
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                continue

            # 只剩一欄
            if left == right:
                for j in range(top, bottom + 1):
                    res.append(matrix[j][left])
                continue

            for i in range(left, right):
                res.append(matrix[top][i])
            for j in range(top, bottom):
                res.append(matrix[j][right])
            for x in range(right, left, -1):
                res.append(matrix[bottom][x])
            for z in range(bottom, top, -1):
                res.append(matrix[z][left])
        
        return res
            