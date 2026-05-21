class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        s = []

        # add to stack in format [temp, index]

        for i in range(len(temperatures) - 1, -1, -1):

            curr = temperatures[i]

            while s and s[-1][0] <= curr:
                s.pop()
            
            if not s:
                temperatures[i] = 0
            
            else:
                temp, index = s[-1]
                temperatures[i] = index - i
            
            s.append([curr, i])
        
        return temperatures
