class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # [2,4,3,2,2,5,1,4]
        if len(arr) <= 1:
            return 1

        l, r = 0, 0
        longest = 1
        curr = 1

        former = 0

        while r < len(arr) - 1:
            first = arr[r]
            second = arr[r + 1]

            if first == second:
                curr = 1
                l = r + 1
                former = 0
            elif first < second:
                if former == 1 or former == 0:
                    curr += 1
                    longest = max(longest, curr)
                else:
                    curr = 2
                    l = r
                former = -1
            else:
                if former == -1 or former == 0:
                    curr += 1
                    longest = max(longest, curr)
                else:
                    curr = 2
                    l = r
                former = 1
            r += 1

        return longest