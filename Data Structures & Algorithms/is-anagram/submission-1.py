class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        for i in range(len(s)):
            if s[i] in d1:
                d1[s[i]] += 1
            else:
                d1[s[i]] = 1

        for i in range(len(t)):
            if t[i] not in d1:
                return False
            elif d1[t[i]] == 0:
                return False
            else:
                d1[t[i]] -= 1
        
        for value in d1.values():
            if value != 0:
                return False

        return True

        