class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # 0 - 1 - 4(A)
        # 1 - 5(A)
        # 0 - 2(A)
        # 0 -> 1 -> 4 -> 1 -> 5 -> 1 -> 0 -> 2 -> 0

        # 0: 1, 2(A)
        # 1: 4(A), 5(A)
        # 2: 3, 6
        # can discard 2

        edgesDict = defaultdict(list)

        for edge in edges:
            pt1, pt2 = edge
            edgesDict[pt1].append(pt2)
            edgesDict[pt2].append(pt1)
        
        
        def dfs(node, parent):
            time = 0
            
            for child in edgesDict[node]:
                if child == parent:
                    continue
                childTime = dfs(child, node)
                if childTime > 0 or hasApple[child]:
                    time += 2 + childTime
            
            return time
        
        return dfs(0, -1)


        