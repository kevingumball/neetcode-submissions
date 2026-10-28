class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLast = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        self.root = TrieNode()
        res = set()
        path = set()

        for word in words:
            node = self.root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.isLast = True
        
        def dfs(node, r, c, cur):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in path):
                return

            if node.isLast:
                res.add(cur)

            if board[r][c] in node.children:
                cur += board[r][c]
                path.add((r,c))
                node = node.children[board[r][c]]
                if node.isLast:
                    res.add(cur)
                dfs(node, r+1, c, cur)
                dfs(node, r-1, c, cur)
                dfs(node, r, c+1, cur)
                dfs(node, r, c-1, cur)
                path.remove((r,c))
                cur = cur[:-1]
            
            return 

        for r in range(ROWS):
            for c in range(COLS):
                dfs(self.root, r, c, "")
        return list(res)

            