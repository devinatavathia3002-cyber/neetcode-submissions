class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # setup
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        l, r = -1, len(nums1) - 1

        length = len(nums1) + len(nums2)
        halfway = (len(nums1) + len(nums2)) // 2

        while True:

            # indexes for nums1 and nums2
            i = ((r - l) // 2) + l # nums1
            j = halfway - i - 2 # nums2

            Aright = nums1[i + 1] if i < len(nums1) - 1 else float("infinity")
            Aleft = nums1[i] if i >= 0 else float("-infinity")
            Bright = nums2[j + 1] if j < len(nums2) - 1 else float("infinity")
            Bleft = nums2[j] if j >= 0 else float("-infinity")

            if Aright >= Bleft and Aleft <= Bright:
                if length % 2 == 0:
                    return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
                else:
                    return min(Aright, Bright)
            
            if Aright < Bleft:
                l = i + 1
            else:
                r = i - 1
            

        
