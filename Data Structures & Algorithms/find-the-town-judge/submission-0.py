class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # incoming - outgoing array
        delta = [0] * n

        for sub in trust:
            per, trusts = sub
            delta[per - 1] -= 1
            delta[trusts - 1] += 1
        
        for i, num in enumerate(delta):
            if num == (n - 1):
                return i + 1

        return -1