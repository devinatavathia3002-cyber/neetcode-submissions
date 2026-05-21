class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabetical = {}
        for word in strs:
            count = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                count[index] += 1
            count = tuple(count)
            alphabetical[count] = alphabetical.get(count, [])
            alphabetical[count].append(word)

        array = []
        for sublist in alphabetical.values():
            array.append(sublist)
        
        return array
                