class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                output = ""
                while stack[-1] != "[":
                    output = stack.pop() + output
                
                stack.pop()
                digit = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                
                stack.append(int(digit) * output)


        return "".join(stack)