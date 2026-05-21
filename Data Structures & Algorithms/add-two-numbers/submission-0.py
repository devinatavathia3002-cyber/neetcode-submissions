# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = l1
        p2 = l2

        carry = 0
        
        dummy = ListNode(-1)
        head = dummy

        while l1 or l2:
            if l1 and l2:
                total = l1.val + l2.val + carry
            elif l1:
                total = l1.val + carry
            else:
                total = l2.val + carry

            newVal = total % 10

            head.next = ListNode(newVal)
            head = head.next

            carry = total // 10
            print(carry)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry > 0:
            head.next = ListNode(carry)
            head = head.next

        return dummy.next

        