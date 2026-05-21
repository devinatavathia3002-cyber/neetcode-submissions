class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
            
        matched = 0

        s1Map = [0] * 26
        s2Map = [0] * 26

        for i in range(len(s1)):
            s1Map[ord(s1[i]) - ord('a')] += 1
            s2Map[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if s1Map[i] == s2Map[i]:
                matched += 1

        if s1Map == s2Map:
            return True
        
        l = 0

        for r in range(len(s1), len(s2)):
    
            if matched == 26:
                return True
            
            s2Map[ord(s2[r]) - ord('a')] += 1
            if s1Map[ord(s2[r]) - ord('a')] == s2Map[ord(s2[r]) - ord('a')]:
                matched += 1
            if s1Map[ord(s2[r]) - ord('a')] == s2Map[ord(s2[r]) - ord('a')] - 1:
                matched -= 1
            
            s2Map[ord(s2[l]) - ord('a')] -= 1
            if s1Map[ord(s2[l]) - ord('a')] == s2Map[ord(s2[l]) - ord('a')]:
                matched += 1
            if s1Map[ord(s2[l]) - ord('a')] == s2Map[ord(s2[l]) - ord('a')] + 1:
                matched -= 1
            
            l += 1
            

        return matched == 26