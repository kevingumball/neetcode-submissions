"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        store = {None : None}
        cur = head

        while cur:
            new = Node(cur.val)
            store[cur] = new
            cur = cur.next
        
        cur = head
        sec = store[head]
        while cur:
            new = store[cur]
            new.next = store[cur.next]
            new.random = store[cur.random]
            cur = cur.next
        return sec
        