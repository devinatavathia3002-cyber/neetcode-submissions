class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        letters = set()
        left = 0
        right = 0
        longest = 0

        while right < len(s):
            if s[right] not in letters:
                letters.add(s[right])
            else:
                while s[left] != s[right]:
                    letters.remove(s[left])
                    left += 1
                left += 1

            print(right)
            longest = max(longest, right - left + 1)
            right += 1

        return longest
