class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # [temp, i]

        for i in range(len(temperatures) - 1, -1, -1):
            curr = temperatures[i]
            while stack and stack[-1][0] <= curr: # look here
                stack.pop()
            if stack:
                temp, popped = stack[-1]
                temperatures[i] = (popped - i)
            else:
                temperatures[i] = 0
            
            stack.append([curr, i])


        return temperatures