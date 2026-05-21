# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        dummy.next = head

        start = head
        behind = dummy

        while n:
            start = start.next
            n -= 1
        
        while start:
            behind = behind.next
            start = start.next
        
        if behind.next == head:
            return head.next

        behind.next = behind.next.next
        return head