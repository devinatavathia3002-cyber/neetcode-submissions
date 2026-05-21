class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        array = [0] * 26

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            array[ord(s[i]) - ord('a')] += 1
            array[ord(t[i]) - ord('a')] -= 1
        
        for val in array:
            if val != 0:
                return False
        return True
        