class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairings = sorted((zip(position, speed)), reverse = True)

        stack = []

        for car in pairings:
                
                speed = ((target - car[0]) / car[1])
                if stack and stack[-1] < speed:
                        stack.append(speed)
                if not stack:
                        stack.append(speed)

        return len(stack)