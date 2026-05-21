class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        res = 0
        total = 0

        for i in range(len(gas)):
            val = gas[i] - cost[i]
            total += val
            if total < 0:
                total = 0
                res = i + 1

        return res