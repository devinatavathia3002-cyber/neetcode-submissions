class FreqStack:

    def __init__(self):
        self.maxVal = 0
        self.freq = {} # maps num to freq
        self.stacks = {} # maps freq to list of nums (stack)

    def push(self, val: int) -> None:
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1
        if self.freq[val] > self.maxVal:
            self.maxVal = self.freq[val]
            self.stacks[self.maxVal] = []
        self.stacks[self.freq[val]].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxVal].pop()
        self.freq[res] -= 1
        if self.stacks[self.maxVal] == []:
            self.maxVal -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()