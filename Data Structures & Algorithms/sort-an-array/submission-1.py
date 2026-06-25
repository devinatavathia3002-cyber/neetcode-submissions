class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort implementation, fwakkk i forgot quick sort
        def merge(L, R):
            subset = []
            i, j = 0, 0

            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    subset.append(L[i])
                    i += 1
                else:
                    subset.append(R[j])
                    j += 1
            
            if i < len(L):
                subset.extend(L[i:])
            
            if j < len(R):
                subset.extend(R[j:])

            return subset

        def mergeSort(arr):
            if len(arr) == 1:
                return arr
            
            middle = len(arr) // 2
            # sepearate right and left
            L = mergeSort(arr[:middle])
            R = mergeSort(arr[middle:])
            return merge(L, R)
        
        return mergeSort(nums)