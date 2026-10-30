class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        lastl, lastr = 0, 0
        substring = ""

        for i in range(len(s)):
            # if odd
            l, r = i, i
            curr = 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                curr += 2
            longest = max(longest, curr - 2)
            if longest == curr - 2:
                lastl, lastr = l + 1, r - 1

            # if even 
            curr = 2
            l, r = i - 1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                curr += 2
            longest = max(longest, curr - 2)
            if longest == curr - 2 and longest > 0:
                lastl, lastr = l + 1, r - 1

        return s[lastl:lastr + 1]