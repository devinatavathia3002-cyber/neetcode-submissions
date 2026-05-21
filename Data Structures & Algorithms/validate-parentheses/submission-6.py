class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False

        stack = []
        chars = {")" : "(", "]" : "[", "}" : "{"}

        for i in range(len(s)):
            if s[i] not in chars:
                stack.append(s[i])
            else:
                if stack:
                    popped = stack.pop()
                    if popped != chars.get(s[i]):
                        return False
                else:
                    return False
        
        if stack:
            return False
        return True