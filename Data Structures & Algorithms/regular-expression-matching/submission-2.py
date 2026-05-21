class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        lenS = len(s)
        lenP = len(p)

        def recurse(l, r):
            if l == lenS and r == lenP:
                return True
            if r == lenP:
                return False
            
            if l == lenS:
                if r < lenP - 1 and p[r + 1] == "*":
                    return recurse(l, r + 2)
                return False
            
            if r < lenP - 1 and p[r + 1] == "*":
                # take or not take
                if s[l] != p[r] and p[r] != ".":
                    return recurse(l, r + 2)
                else:
                    return recurse(l + 1, r) or recurse(l, r + 2)
            
            elif s[l] == p[r] or p[r] == ".":
                return recurse(l + 1, r + 1)
            
            else:
                return False
        
        return recurse(0, 0)

