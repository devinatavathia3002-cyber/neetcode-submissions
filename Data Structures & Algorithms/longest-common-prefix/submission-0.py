class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # horizontal and vertical implementation

        # horizontal

        prefix = strs[0]

        for word in strs:
            
            j = 0
            for i in range(min(len(prefix), len(word))):
                if prefix[i] != word[i]:
                    break
                j += 1
            
            prefix = prefix[0:j]

        return prefix
        