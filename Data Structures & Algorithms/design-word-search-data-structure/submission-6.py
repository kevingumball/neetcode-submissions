class TreeNode:
    def __init__(self):
        self.children = {}
        self.isLast = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TreeNode()
            cur = cur.children[w]
        cur.isLast = True
        return

    def search(self, word: str) -> bool:
  
        def dfs(cur, i):

            for j in range(i, len(word)):
                if word[j] == ".":
                    for child in cur.children.values():
                        if dfs(child, j + 1):
                            return True
                    return False

                elif word[j] not in cur.children:
                    return False
                
                else:
                    cur = cur.children[word[j]]
            return cur.isLast

        return dfs(self.root, 0)

