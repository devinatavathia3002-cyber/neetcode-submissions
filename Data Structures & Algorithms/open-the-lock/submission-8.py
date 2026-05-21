class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if "0000" in deadends:
            return -1
            
        visited = set()
        for num in deadends:
            visited.add(num)
        
        q = deque()
        q.append("0000")
        visited.add("0000")

        output = 0

        while q:
            length = len(q)
            for i in range(length):
                popped = q.popleft()
                if popped == target:
                    return output

                for j in range(4):
                    pos = (int(popped[j]) + 1) % 10
                    minus = (int(popped[j]) - 1) % 10
                    down = popped[:j] + str(minus) + popped[j + 1:]
                    up = popped[:j] + str(pos) + popped[j + 1:]
                    if up not in visited:
                        q.append(up)
                        visited.add(up)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)
            output += 1

        return -1