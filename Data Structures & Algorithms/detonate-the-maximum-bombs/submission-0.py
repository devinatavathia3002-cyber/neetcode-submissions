from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # first, setup adj list
        longest = 0
        adj = defaultdict(list)

        for i in range(len(bombs)):
            start, end, radius = bombs[i]
            for j in range(i + 1, len(bombs)):
                start2, end2, radius2 = bombs[j]
                distance = ((start2 - start) ** 2 + (end2 - end) ** 2)
                if distance <= radius ** 2:
                    adj[i].append(j)
                if distance <= radius2 ** 2:
                    adj[j].append(i)
        
        def dfs(node, visited):
            visited.add(node)
            total = 0
            for bomb in adj[node]:
                if bomb not in visited:
                    visited.add(bomb)
                    total += 1 + dfs(bomb, visited)
            return total
        

        for i in range(len(bombs)):
            longest = max(longest, 1 + dfs(i, set()))
        
        return longest
