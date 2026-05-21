class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # [1,2,3] -> gas
        # [2,3,2] -> cost

        if sum(gas) < sum(cost):
            return -1
        
        output = 0
        total = 0

        for i in range(len(gas)):
            val = gas[i] - cost[i]
            total += val
            if total < 0:
                total = 0
                output = i + 1

        return output
        

