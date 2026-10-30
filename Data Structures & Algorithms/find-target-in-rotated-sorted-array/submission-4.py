class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # index of length - num of rotations
        # [3,4,5,6,0,1,2,3]

        # two pass solution
        # first, find the peak
        peak = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                peak = i
        
        print(peak)
        l, r = 0, len(nums) - 1
        if peak != -1:
            if target <= nums[peak] and target >= nums[0]:
                r = peak
            else:
                l = peak + 1

        
        # do a basic binary search
        while l <= r:
            mid = ((r - l) // 2) + l
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1