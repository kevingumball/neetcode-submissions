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
        oldtonew[node] = Node(node.val)
        q.append(node)

        while q:
            root = q.popleft()
            for nei in root.neighbors:
                if nei not in oldtonew:
                    oldtonew[nei] = Node(nei.val)
                    q.append(nei)
                oldtonew[root].neighbors.append(oldtonew[nei])

        
        return oldtonew[node]

        