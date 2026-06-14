class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        arr = [[] for _ in range(4)]

        total = sum(matchsticks)
        sideLen = total // 4

        if total % 4 != 0:
            return False

        matchsticks.sort(reverse = True)
        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sum(arr[j]) + matchsticks[i] > sideLen:
                    continue
                arr[j].append(matchsticks[i])
                if backtrack(i + 1):
                    return True
                arr[j].pop()
            
            return False
        
        return backtrack(0)