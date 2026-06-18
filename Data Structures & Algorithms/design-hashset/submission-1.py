class MyHashSet:

    def __init__(self):
        self.MyHashSet = []

    def add(self, key: int) -> None:
        found = False
        for i in range(len(self.MyHashSet)):
            if self.MyHashSet[i] == key:
                found = True
        if not found:
            self.MyHashSet.append(key)

    def remove(self, key: int) -> None:
        hold = -1
        for i in range(len(self.MyHashSet)):
            if self.MyHashSet[i] == key:
                hold = i
        if hold == -1:
            return 
        self.MyHashSet[-1], self.MyHashSet[hold] = self.MyHashSet[hold], self.MyHashSet[-1]
        self.MyHashSet = self.MyHashSet[:-1]

    def contains(self, key: int) -> bool:
        for i in range(len(self.MyHashSet)):
            if self.MyHashSet[i] == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)