class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l, res, maxf = 0, 0, 0

        for r in range(len(s)):
            curr = s[r]
            count[curr] += 1
            maxf = max(maxf, count[curr])

            while (r - l + 1 - maxf) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

        
