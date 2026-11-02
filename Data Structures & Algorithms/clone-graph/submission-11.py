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
        q = deque()
        q.append(node)
        new = Node(node.val)
        oldtonew[node] = new

        while q:
            root = q.popleft()
            for nei in root.neighbors:
                if nei not in oldtonew:
                    new = Node(nei.val)
                    oldtonew[nei] = new
                    q.append(nei)
                oldtonew[root].neighbors.append(oldtonew[nei])

        return oldtonew[node]

