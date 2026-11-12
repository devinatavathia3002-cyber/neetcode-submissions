class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:

        visited1 = set()
        visited2 = set()

        adj = defaultdict(list)

        distances1 = defaultdict(int)
        distances2 = defaultdict(int)

        smallestNode, smallestDist = float("inf"), float("inf")

        q1, q2 = deque(), deque()

        q1.append((node1, 0))
        q2.append((node2, 0))
        visited1.add(node1)
        visited2.add(node2)

        # setup adj list
        for i in range(len(edges)):
            adj[i].append(edges[i])

        # from node1
        while q1:
            length = len(q1)
            for i in range(length):
                node, distance = q1.popleft()
                distances1[node] = distance
                for edge in adj[node]:
                    if edge not in visited1:
                        q1.append((edge, distance + 1))
                        visited1.add(edge)

        # from node2
        while q2:
            length = len(q2)
            for i in range(length):
                node, distance = q2.popleft()
                distances2[node] = distance
                for edge in adj[node]:
                    if edge not in visited2:
                        q2.append((edge, distance + 1))
                        visited2.add(edge)

        # get the res
        for edge in range(len(edges)):
            if edge in distances1 and edge in distances2:
                dist1, dist2 = distances1[edge], distances2[edge]
                dist = max(dist1, dist2)
                if dist <= smallestDist:
                    if dist == smallestDist:
                        if edge < smallestNode:
                            smallestNode = edge
                    else:
                        smallestNode, smallestDist = edge, dist
        
        if smallestNode == float("inf"):
            return -1
        return smallestNode

