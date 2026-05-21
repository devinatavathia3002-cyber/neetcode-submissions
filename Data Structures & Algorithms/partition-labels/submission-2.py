class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        output = []
        l, r = 0, 0

        count = defaultdict(int)
        for i in range(len(s)):
            char = s[i]
            count[char] = i

        while r < len(s):

            i = l
            while i <= r:
                curr = s[i]
                r = max(r, count[curr])  # get farthest index
                i += 1
            
            output.append(r - l + 1)
            l = r + 1
            r += 1

        return output