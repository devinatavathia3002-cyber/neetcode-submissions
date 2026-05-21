class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # split by backslash
        paths = path.split("/")

        stack = []

        for c in paths:
            if c == "..":
                if stack:
                    stack.pop()
            elif c != "" and c != ".":
                stack.append(c)

        return "/" + "/".join(stack)