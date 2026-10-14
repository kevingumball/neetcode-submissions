# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        sec = slow.next
        slow.next = None

        prev = None
        cur = sec
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        sec = prev
        dummy = first
        while first and sec:
            tmp1 = first.next
            tmp2 = sec.next
            first.next = sec
            sec.next = tmp1
            first = tmp1
            sec = tmp2
        
    
        