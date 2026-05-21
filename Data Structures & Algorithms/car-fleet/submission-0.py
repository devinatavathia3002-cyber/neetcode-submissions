class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        together = sorted(zip(position, speed), reverse = True)

        stack = []

        for i in range(len(together)):
            distance = (target - together[i][0]) / together[i][1]

            if not stack or stack[-1] < distance:
                stack.append(distance)
            
        return len(stack)