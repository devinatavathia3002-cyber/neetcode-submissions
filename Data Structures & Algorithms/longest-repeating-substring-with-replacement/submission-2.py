class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        maxf = defaultdict(int)
        maxVal = 0

        windowLength = 0

        l = 0
        for r in range(len(s)):
            curr = s[r]
            maxf[curr] += 1

            if maxf[curr] > maxVal:
                maxVal = maxf[curr]

            while ((r - l + 1) - maxVal) > k:
                maxf[s[l]] -= 1
                l += 1
            
            windowLength = max(windowLength, (r - l + 1))

        return windowLength
        