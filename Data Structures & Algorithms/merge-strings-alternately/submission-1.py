class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        length = min(len(word1), len(word2))

        w1 = 0
        w2 = 0

        output = ""
        loop = 0

        while w1 < length and w2 < length:
            if loop % 2 == 0:
                output += word1[w1]
                w1 += 1
            else:
                output += word2[w2]
                w2 += 1
            
            loop += 1

        if w2 < len(word2):
            output += word2[w2:len(word2)]
        if w1 < len(word1):
            output += word1[w1:len(word1)]
        
        return output