class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # edge case
        if t == "":
            return ""

        tMap = [0] * 128
        sMap = [0] * 128
        
        length = len(set(t))
        have = 0

        shortestLen = float("infinity")
        substring = ""


        for letter in t:
            tMap[ord(letter) - ord('a')] += 1
        
        l, r = 0, 0

        while r < len(s):
            curr = s[r]
            sMap[ord(curr) - ord('a')] += 1

            if sMap[ord(curr) - ord('a')] == tMap[ord(curr) - ord('a')]:
                have += 1
            
            while have == length:
                shortestLen = min(shortestLen, r - l + 1)
                if shortestLen == (r - l + 1):
                    substring = s[l:r + 1]
                
                curr = s[l]
                sMap[ord(curr) - ord('a')] -= 1
                if sMap[ord(curr) - ord('a')] < tMap[ord(curr) - ord('a')]:
                    have -= 1
                l += 1
            
            r += 1
        
        return substring
