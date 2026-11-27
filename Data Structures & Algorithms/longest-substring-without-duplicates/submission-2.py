class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        curr = set()

        l, r = 0, 0

        while r < len(s):
            char = s[r]
            if char in curr:
                while l < r and s[l] != char:
                    curr.remove(s[l])
                    l += 1
                l += 1
            else:
                curr.add(char)
                longest = max(longest, r - l + 1)       

            r += 1 

        return longest