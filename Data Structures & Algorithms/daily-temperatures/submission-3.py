class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        s = []
        fin = [0] * len(temperatures)

        # top of stack arr [temp, index]

        for i in range(len(temperatures)):

            curr = temperatures[i]

            while s and s[-1][0] < curr:
                temp, index = s.pop()
                fin[index] = (i - index)
            
            s.append([curr, i])

        return fin

