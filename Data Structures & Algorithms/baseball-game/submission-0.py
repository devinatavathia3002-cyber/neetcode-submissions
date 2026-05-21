class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []

        for i in range(len(operations)):
            if operations[i] == "D":
                val = (2 * stack[-1])
                stack.append(val)
            elif operations[i] == "+":
                val = (stack[-1] + stack[-2])
                stack.append(val)
            elif operations[i] == "C":
                stack.pop()
            else:
                stack.append(int(operations[i]))

        return sum(stack)