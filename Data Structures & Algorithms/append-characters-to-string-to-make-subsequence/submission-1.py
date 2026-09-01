class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s1, t1 = 0, 0
        ct = 0

        while s1 < len(s) and t1 < len(t):
            sChar, tChar = s[s1], t[t1]
            while sChar != tChar and s1 < len(s):
                s1 += 1
                if s1 < len(s):
                    sChar = s[s1]
            if s1 < len(s):
                t1 += 1
                s1 += 1
        
        if t1 < len(t):
            ct += (len(t) - t1)
        
        print(t1)
        return ct