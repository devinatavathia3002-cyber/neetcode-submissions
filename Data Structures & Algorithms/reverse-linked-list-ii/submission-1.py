# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        curr = head

        remaining = left

        while remaining > 1:
            prev = curr
            curr = curr.next
            remaining -= 1
        
        remaining = (right - left)
        start = curr

        while remaining > 0:
            curr = curr.next 
            remaining -= 1
        
        end = curr
        post = curr.next

        # prev and post will connect to to our reversed list in the end
        dummy = None
        curr = start

        while curr != post:
            future = curr.next
            curr.next = dummy
            dummy = curr
            curr = future
        
        if prev:
            prev.next = end
        start.next = post

        if left == 1:
            return end
        return head


