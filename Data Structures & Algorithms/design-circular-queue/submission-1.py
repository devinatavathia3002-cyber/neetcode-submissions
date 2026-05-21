class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.head = Node(-1)
        self.tail = Node(-1)

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        newNode = Node(value)
        prevNode = self.tail.prev

        prevNode.next = newNode
        newNode.prev = prevNode

        newNode.next = self.tail
        self.tail.prev = newNode

        self.capacity -= 1
        return True

    def deQueue(self) -> bool:
        if self.head.next == self.tail:
            return False
        postNode = self.head.next.next
        self.head.next = postNode
        postNode.prev = self.head

        self.capacity +=1
        return True

    def Front(self) -> int:
        if self.head.next == self.tail:
            return -1
        return self.head.next.val

    def Rear(self) -> int:
        if self.tail.prev == self.head:
            return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        if self.tail.prev == self.head:
            return True
        return False

    def isFull(self) -> bool:
        if self.capacity == 0:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()