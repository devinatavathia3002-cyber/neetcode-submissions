class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
            
        mapp = {"2" : "abc",
                "3" : "def",
                "4" : "ghi",
                "5" : "jkl",
                "6" : "mno",
                "7" : "pqrs",
                "8" : "tuv",
                "9" : "wxyz"}

        res = []

        def dfs(index, sub):
            nonlocal res

            if len(sub) == len(digits):
                res.append("".join(sub.copy()))
                return
  
            for i in range(0, len(mapp[digits[index]])):
                sub.append(mapp[digits[index]][i])
                dfs(index + 1, sub)
                sub.pop()
        
        dfs(0, [])
        return res