class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashMap:

    def __init__(self):
        self.container = [ListNode(0) for i in range(pow(10, 4))]

    def put(self, key: int, value: int) -> None:
        curr = self.container[key % len(self.container)]

        while curr.next:
            if curr.next.key[0] == key:
                curr.next = ListNode([key, value])
                return
            curr = curr.next
        curr.next = ListNode([key, value])

    def get(self, key: int) -> int:
        curr = self.container[key % len(self.container)]

        while curr.next:
            if curr.next.key[0] == key:
                return curr.next.key[1]
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        curr = self.container[key % len(self.container)]

        while curr.next:
            if curr.next.key[0] == key:
                curr.next = curr.next.next
                return
            curr = curr.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)