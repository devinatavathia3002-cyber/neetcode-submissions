class ListNode:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.MRU, self.LRU = ListNode(0, 0), ListNode(0, 0)
        # front is LRU, back is MRU
        self.MRU.prev, self.LRU.next = self.LRU, self.MRU
    
    def delete(self, key):
        node = self.cache[key]
        prev, after = node.prev, node.next
        prev.next, after.prev = after, prev
    
    def insert(self, key):
        # inserting at the back
        node = self.cache[key]
        prev, after = self.MRU.prev, self.MRU

        prev.next, after.prev = node, node
        node.next, node.prev = after, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(key)
            self.insert(key)
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.delete(key)
            self.insert(key)
        else:
            self.cache[key] = ListNode(key, value)
            self.insert(key)
            
        # reassign capacity if needed
        if len(self.cache) > self.capacity:
            mapKey = self.LRU.next.key
            self.delete(mapKey)
            del self.cache[mapKey]

