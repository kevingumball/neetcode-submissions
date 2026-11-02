"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldtonew = {}

        def dfs(node):
            new = Node(node.val)
            oldtonew[node] = new
            for nei in node.neighbors:
                if nei in oldtonew:
                    new.neighbors.append(oldtonew[nei])
                else:
                    new.neighbors.append(dfs(nei))
            return new

        return dfs(node)
        