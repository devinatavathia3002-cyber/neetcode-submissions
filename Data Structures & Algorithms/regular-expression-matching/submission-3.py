class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        lenS = len(s)
        lenP = len(p)
        cache = {}

        def recurse(l, r):
            if l == lenS and r == lenP:
                return True
            if (l, r) in cache:
                return cache[(l, r)]

            if r == lenP:
                cache[(l, r)] = False
            elif l == lenS:
                if r < lenP - 1 and p[r + 1] == "*":
                    return recurse(l, r + 2)
                cache[(l, r)] = False
            
            elif r < lenP - 1 and p[r + 1] == "*":
                if s[l] != p[r] and p[r] != ".":
                    cache[(l, r)] = recurse(l, r + 2)
                else:
                    cache[(l, r)] = (recurse(l + 1, r) or recurse(l, r + 2))
            
            elif s[l] == p[r] or p[r] == ".":
                cache[(l, r)] = recurse(l + 1, r + 1)
            
            else:
                cache[(l, r)] = False
            
            return cache[(l, r)]
        
        return recurse(0, 0)

