class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq = defaultdict(int)
        length = len(nums)

        for num in nums:
            freq[num] += 1
        
        for num, count in freq.items():
            if count > length / 2:
                return num
        
        return -1