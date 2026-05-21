class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        visited = set(deadends)

        beg = {"0000"}
        end = {target}

        steps = 0

        if target in visited or "0000" in visited:
            return -1

        while beg and end:
            if len(beg) > len(end):
                beg, end = end, beg
            
            temp = set()
            steps += 1

            for lock in beg:
                
                for j in range(4):
                    newVal1 = lock[:j] + str((int(lock[j]) + 1) % 10) + lock[j + 1:]
                    newVal2 = lock[:j] + str((int(lock[j]) - 1 + 10) % 10) + lock[j + 1:]

                    if newVal1 in end or newVal2 in end:
                        return steps
                    
                    if newVal1 not in visited:
                        visited.add(newVal1)
                        temp.add(newVal1)
                    
                    if newVal2 not in visited:
                        visited.add(newVal2)
                        temp.add(newVal2)

            beg = temp

        return -1


