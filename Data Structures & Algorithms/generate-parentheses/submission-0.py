class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []

        def backtrack(opening, close):
            nonlocal stack
            nonlocal res

            if opening == close == n:
                res.append("".join(stack.copy()))
                return
            
            if opening < n:
                stack.append('(')
                backtrack(opening + 1, close)
                stack.pop()
            
            if close < opening:
                stack.append(')')
                backtrack(opening, close + 1)
                stack.pop()
            

        backtrack(0, 0)
        return res