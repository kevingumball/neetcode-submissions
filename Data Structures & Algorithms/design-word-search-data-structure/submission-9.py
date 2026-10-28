class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLast = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isLast = True
        return

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i >= len(word):
                return node.isLast 
            if word[i] != ".":
                if word[i] not in node.children:
                    return False
                else:
                    return dfs(node.children[word[i]], i + 1)
            else:
                for j in node.children.values():
                    if dfs(j, i+1):
                        return True
            return False

        return dfs(self.root, 0)


