class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for rock in asteroids:
            
            while stack and rock < 0 and stack[-1] > 0:
                top = stack[-1]
                if abs(top) > abs(rock):
                    rock = 0
                elif abs(top) < abs(rock):
                    stack.pop()
                else:
                    stack.pop()
                    rock = 0
            
            if rock:
                stack.append(rock)
        
        return stack
            

