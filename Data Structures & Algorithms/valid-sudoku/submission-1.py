class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = 9, 9
        row = [[] for i in range(9)]
        col = [[] for i in range(9)]
        box = [[[] for _ in range(3)] for _ in range(3)]
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in box[i // 3][j // 3]:
                    return False
                row[i].append(board[i][j])
                col[j].append(board[i][j])
                box[i // 3][j // 3].append(board[i][j])
        return True

        