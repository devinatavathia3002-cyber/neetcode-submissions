# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        dummy.next = head
        prevNode = dummy

        while True:
            start = prevNode.next
            curr = prevNode

            # find if we have to break or not
            counter = k
            print(curr.val)
            while curr and counter > 0:
                curr = curr.next
                counter -= 1
            if counter > 0 or curr is None:
                break
            
            postNode = curr.next

            #prevNode, start, curr, postNode

            prev = None
            curr = start

            while curr != postNode:
                future = curr.next
                curr.next = prev
                prev = curr
                curr = future
            
            prevNode.next = prev
            start.next = postNode

            prevNode = start

        return dummy.next