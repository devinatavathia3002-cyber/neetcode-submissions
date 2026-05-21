class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabetical = {}
        for string in strs:
            key = ''.join(sorted(string))
            alphabetical[key] = alphabetical.get(key, []);
            alphabetical[key].append(string)

        array = []
        for sublist in alphabetical.values():
            array.append(sublist)
        
        return array
                