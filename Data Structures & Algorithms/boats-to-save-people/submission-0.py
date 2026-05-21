class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        # implement count sort

        maximum = max(people)
        length = len(people)
        count = [0] * (maximum + 1)

        for num in people:
            count[num] += 1
        
        pointer = 0 # pointer for count arr
        for i in range(length):
            while count[pointer] == 0:
                pointer += 1
            
            people[i] = pointer
            count[pointer] -= 1

        # pair the weightiest person with least weighiest
        l = 0
        r = length - 1
        output = 0

        while l <= r:
            leftover = (limit - people[r])

            if people[l] <= leftover:
                l += 1
            
            r -= 1
            output += 1
        
        return output