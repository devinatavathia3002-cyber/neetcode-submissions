class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res = []

        def backtrack(i, sub):
            nonlocal res
            if i >= len(s):
                if len(sub) > 0:
                    res.append(sub)
                return
            
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict:
                    backtrack(j + 1, sub + " " + s[i:j + 1] if sub else sub + s[i:j + 1])
            return

        backtrack(0, "")
        return res