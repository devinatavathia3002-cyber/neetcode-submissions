class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # horizontal and vertical implementation

        # horizontal

        prefix = strs[0]

        for word in strs:
            
            j = 0
            while j < (min(len(prefix), len(word))):
                if prefix[j] != word[j]:
                    break
                j += 1
            
            prefix = prefix[0:j]

        return prefix
        