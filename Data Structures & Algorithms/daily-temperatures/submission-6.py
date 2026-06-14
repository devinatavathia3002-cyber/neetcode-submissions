class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)

        for i in range(length - 1, - 1, -1):
            curr = temperatures[i]
            if len(stack) == 0:
                temperatures[i] = 0
            else:
                while len(stack) and stack[-1][0] <= curr:
                    stack.pop()
                if len(stack) == 0:
                    temperatures[i] = 0
                else:
                    temperatures[i] = stack[-1][1] - i
            stack.append((curr, i))

        return temperatures