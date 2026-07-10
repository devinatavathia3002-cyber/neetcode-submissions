class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        output = []

        def putPeriods(dots, i, sub):
            if dots == 4 and i == len(s):
                output.append(sub[:-1])
                return
            if dots > 4:
                return
            if i > len(s):
                return
            
            for j in range(i, min(len(s), i + 3)):
                curr = s[i:j + 1]
                if 0 <= int(curr) <= 255:
                    if j > i and s[i] == "0":
                        break
                    else:
                        putPeriods(dots + 1, j + 1, sub + curr + ".")

                else:
                    continue
        
        putPeriods(0, 0, "")

        return output