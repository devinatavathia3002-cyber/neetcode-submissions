# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # fast and slow pointer
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        p1 = head

        # break link between first and second half of list
        curr = slow.next
        slow.next = None

        # reverse second half of list
        prev = None

        while curr:
            future = curr.next
            curr.next = prev

            prev = curr
            curr = future
        
        p2 = prev

        # now we combine
        curr = p1
        while p1 and p2:
            if curr == p1:
                p1 = p1.next
                curr.next = p2
            else:
                p2 = p2.next
                curr.next = p1
            curr = curr.next
        
        if p1:
            curr.next = p1.next
        if p2:
            curr.next = p2.next
        
        # return nothing