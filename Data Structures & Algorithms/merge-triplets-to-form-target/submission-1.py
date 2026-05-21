class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        bool1 = False
        bool2 = False
        bool3 = False

        f, m, l = target

        for triplet in triplets:
            a, b, c = triplet
            if a > f or b > m or c > l:
                continue
            else:
                if a == f:
                    bool1 = True
                if b == m:
                    bool2 = True
                if c == l:
                    bool3 = True

        return bool1 and bool2 and bool3