class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ways to do this problem 
        # hashmap, hashtable with frequency counter

        # hashtable implementation
        frequency = [0] * 26

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            frequency[ord(s[i]) - ord('a')] += 1
            frequency[ord(t[i]) - ord('a')] -= 1
        
        for num in frequency:
            if num != 0:
                return False
        
        return True
        