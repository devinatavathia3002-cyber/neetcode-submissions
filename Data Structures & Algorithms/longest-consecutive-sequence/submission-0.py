class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        no_dupes = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in no_dupes:
                length = 1
                count = 1
                while (num + count) in no_dupes:
                    length += 1
                    count += 1
                longest = max(length, longest)

        return longest