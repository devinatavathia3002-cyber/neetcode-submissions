# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find middle of list, reverse second half
        if not head or not head.next:
            return
        
        fast = head.next
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        prev = None
        curr = head2

        while curr is not None:
            future = curr.next
            curr.next = prev
            prev = curr
            curr = future
        
        head2 = prev

        # reorder list
        f = head
        s = head2

        while s is not None:
            f1 = f.next
            s2 = s.next

            f.next = s
            s.next = f1

            f = f1
            s = s2
        