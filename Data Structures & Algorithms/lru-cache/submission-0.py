class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.front = Node(0, 0)
        self.back = Node(0, 0)

        self.front.next = self.back
        self.back.prev = self.front
        
    def insert(self, node):
        past = self.back.prev

        past.next = node
        node.prev = past

        self.back.prev = node
        node.next = self.back
    
    def remove(self, node):
        past = node.prev
        future = node.next

        past.next = future
        future.prev = past

    def get(self, key: int) -> int:
        if key in self.cache:
            curr = self.cache[key]
            self.remove(curr)
            self.insert(curr)
            return curr.val
        return -1

    def put(self, key: int, value: int) -> None:
        newNode = Node(key, value)

        if key in self.cache:
            curr = self.cache[key]
            self.remove(curr)
            self.insert(newNode)
        else:
            if len(self.cache) == self.capacity:
                remVal = self.front.next
                self.remove(remVal)
                self.cache.pop(remVal.key)
            self.insert(newNode)
        
        self.cache[key] = newNode

