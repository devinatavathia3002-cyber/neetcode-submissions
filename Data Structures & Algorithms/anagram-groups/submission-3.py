class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # using a character map

        d = defaultdict(list)
        for i in range(len(strs)):
            chars = [0] * 26
            for s in strs[i]:
                chars[ord(s) - ord('a')] += 1
            d[tuple(chars)].append(strs[i])
        
        return list(d.values())
            
        