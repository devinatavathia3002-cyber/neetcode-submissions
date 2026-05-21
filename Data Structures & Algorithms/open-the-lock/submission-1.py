class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        # let's try this with standard bfs first
        visited = set(deadends)
        q = deque()
        q.append("0000")
        steps = 0

        # edge case
        if target in deadends or "0000" in deadends:
            return -1

        # main loop
        while q:
            steps += 1
            for j in range(len(q)):
                val = q.popleft()

                for i in range(4):
                    digit1 = (int(val[i]) + 1) % 10
                    val1 = val[:i] + str(digit1) + val[i + 1:]

                    digit2 = (int(val[i]) - 1 + 10) % 10
                    val2 = val[:i] + str(digit2) + val[i + 1:]

                    if val1 == target or val2 == target:
                        return steps
                    if val1 not in visited:
                        q.append(val1)
                        visited.add(val1)
                    if val2 not in visited:
                        q.append(val2)
                        visited.add(val2)

        return -1