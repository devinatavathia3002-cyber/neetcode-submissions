class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(log)
        
        return len(stack)