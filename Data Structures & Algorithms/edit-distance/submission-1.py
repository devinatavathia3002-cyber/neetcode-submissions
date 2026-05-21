class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = {}
        def recurse(i1, i2):
            if i2 == len(word2):
                return len(word1) - i1 # amount of deletions
            if i1 == len(word1):
                return len(word2) - i2 # amount of insertions
            if (i1, i2) in dp:
                return dp[(i1, i2)]

            if word1[i1] != word2[i2]:
                # explore 3 options with 1 + and min() function
                dp[(i1, i2)] = min(1 + recurse(i1, i2 + 1), 
                                   1 + recurse(i1 + 1, i2), 
                                   1 + recurse(i1 + 1, i2 + 1))
            else:
                dp[(i1, i2)] = recurse(i1 + 1, i2 + 1)
            
            return dp[(i1, i2)]
            
        return recurse(0, 0)

