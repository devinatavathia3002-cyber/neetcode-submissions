class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        randC = {}
        randO = {}

        dummy = Node(-1)

        p1 = dummy
        p2 = head

        while p2:
            node = Node(p2.val)
            p1.next = node

            randC[node] = p2
            randO[p2] = node

            p1 = p1.next
            p2 = p2.next

        p3 = dummy.next

        while p3:
            original = randC[p3]
            originalRand = original.random

            if originalRand:
                p3.random = randO[originalRand]

            p3 = p3.next

        return dummy.next