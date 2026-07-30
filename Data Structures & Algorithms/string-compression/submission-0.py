class Solution:
    def compress(self, chars: List[str]) -> int:
        # read, write, groupings
        i, index, group = 0, 0, 0
        
        while i < len(chars):
            while group < len(chars) and chars[i] == chars[group]:
                group += 1
            length = group - i
            chars[index] = chars[i]
            index += 1

            if length > 1:
                for j in range(len(str(length))):
                    chars[index] = (str(length)[j])
                    index += 1
            i = group
        
        return index