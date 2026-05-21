class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left, longest = 0, 0
        frequency = defaultdict(int)
        greatestFrequency = 0

        for i in range(len(s)):
            
            curr = s[i]
            frequency[s[i]] += 1
            greatestFrequency = max(greatestFrequency, frequency[s[i]])

            while ((i - left + 1) - greatestFrequency) > k:
                frequency[s[left]] -= 1
                left += 1
            
            longest = max(longest, (i - left + 1))

        return longest