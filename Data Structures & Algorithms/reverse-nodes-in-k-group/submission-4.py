# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        def findkth(node, k):
            while node and k > 0:
                node = node.next
                k -= 1
            return node

        while True:
            cur = groupPrev.next
            kth = findkth(groupPrev, k)
            if not kth:
                return dummy.next

            groupNext = kth.next
            prev = groupNext

            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp = groupPrev.next
            groupPrev.next = prev
            groupPrev = tmp

        
        