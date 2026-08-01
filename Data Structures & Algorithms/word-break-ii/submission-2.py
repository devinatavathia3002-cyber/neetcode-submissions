class Solution: 
    def wordBreak(self, s, wordDict):
        output = []
        memo = {}

        def recurse(i):
            if i in memo:
                return memo[i]
            if i >= len(s):
                return [""]
            
            res = []
            for word in wordDict:
                length = len(word)
                if i + length <= len(s) and s[i:i + length] == word:
                    suffixes = recurse(i + length)
                    for suffix in suffixes:
                        if suffix:
                            res.append(word + " " + suffix)
                        else:
                            res.append(word)
            
            memo[i] = res
            return res

        return recurse(0)