class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # output = 0
        
        # def dfs(sIndex, tIndex):
        #     nonlocal output
        #     if tIndex == len(t):
        #         output += 1
        #         return
        #     if sIndex == len(s):
        #         return 
            
        #     if s[sIndex] != t[tIndex]:
        #         dfs(sIndex + 1, tIndex)
        #     else:
        #         dfs(sIndex + 1, tIndex + 1)
        #         dfs(sIndex + 1, tIndex)
        
        # dfs(0, 0)
        # return output

        # top-down memoization
        dp = {}
        lenS = len(s)
        lenT = len(t)

        def dfs(sIndex, tIndex):
            if tIndex == lenT:
                return 1
            if sIndex == lenS:
                return 0
            if (sIndex, tIndex) in dp:
                return dp[(sIndex, tIndex)]
            
            res = dfs(sIndex + 1, tIndex)
            if s[sIndex] == t[tIndex]:
                res += dfs(sIndex + 1, tIndex + 1)
            dp[(sIndex, tIndex)] = res
            return res

        return dfs(0, 0)