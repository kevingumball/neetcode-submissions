class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLast = False
    
    def addword(self, word):
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isLast = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        root = TrieNode()
        for w in words:
            root.addword(w)
        res = set()
        visit = set()

        def dfs(r, c, node, word):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visit or board[r][c] not in node.children):
                return False
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isLast:
                res.add(word)

            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)

        