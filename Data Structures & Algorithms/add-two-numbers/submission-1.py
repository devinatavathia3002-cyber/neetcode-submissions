# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ptr1, ptr2, ptr3 = l1, l2, ListNode(-1)
        res = ptr3

        while ptr1 or ptr2:
            total = 0
            if ptr1:
                total += ptr1.val
                ptr1 = ptr1.next
            if ptr2:
                total += ptr2.val
                ptr2 = ptr2.next
            if carry:
                total += carry
                carry = 0
            
            if total > 9:
                carry = 1
                total = total % 10
            
            ptr3.next = ListNode(total)
            ptr3 = ptr3.next

        if carry:
            ptr3.next = ListNode(carry)
        return res.next
        
