class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # monotonic stack
        s = []

        for i in range(len(temperatures) - 1, -1, -1):
            if len(s) == 0:
                s.append([temperatures[i], i])
                temperatures[i] = 0
            
            else:
                while s and s[-1][0] <= temperatures[i]:
                    s.pop()
                
                if len(s) == 0:
                    s.append([temperatures[i], i])
                    temperatures[i] = 0
                else:
                    warmer, index = s[-1]
                    s.append([temperatures[i], i])
                    temperatures[i] = (index - i)
        
        return temperatures