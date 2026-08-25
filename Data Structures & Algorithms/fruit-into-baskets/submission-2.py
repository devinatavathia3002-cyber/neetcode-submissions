class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #[1, 2, 1, 1, 1, 3, 1]
        num1, num2 = -1, -1
        last1, last2 = -1, -1

        longest = 0
        l, r = 0, 0

        while r < len(fruits):
            curr = fruits[r]
            if curr != num1 and curr != num2:
                if num1 == -1:
                    num1 = curr
                    last1 = r
                elif num2 == -1:
                    num2 = curr
                    last2 = r
                else:
                    longest = max(longest, r - l)
                    smallest = min(last1, last2)
                    l = smallest + 1
                    if smallest == last1:
                        num1 = curr
                        last1 = r
                    else:
                        num2 = curr
                        last2 = r
            elif curr == num1:
                last1 = r
            else:
                last2 = r
            
            r += 1
        
        longest = max(longest, r - l)
        return longest