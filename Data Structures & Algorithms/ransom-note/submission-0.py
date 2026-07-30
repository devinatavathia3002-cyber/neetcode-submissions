class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charArr = [0] * 26

        for char in ransomNote:
            index = ord(char) - ord('a')
            charArr[index] += 1
        
        for char in magazine:
            index = ord(char) - ord('a')
            charArr[index] -= 1
        
        for i in range(len(charArr)):
            if charArr[i] > 0:
                return False
        
        return True