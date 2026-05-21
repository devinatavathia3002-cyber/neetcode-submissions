class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ways to do this problem 
        # hashmap, hashtable with frequency counter

        # hashtable implementation
        frequency = [0] * 26

        for letter in s:
            frequency[ord(letter) - ord('a')] += 1
        
        for letter in t:
            frequency[ord(letter) - ord('a')] -= 1
        
        for number in frequency:
            if number != 0:
                return False
        
        
        return True
        