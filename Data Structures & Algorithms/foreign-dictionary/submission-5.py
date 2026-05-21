class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # form adjacency list
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for word in words:
            for c in word:
                indegree[c] = 0

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            if len(w2) < len(w1) and w1[:len(w2)] == w2:
                return ""
            
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].append(w2[j])
                        indegree[w2[j]] += 1
                    break
        
        # conduct topo sort
        q = deque()
        for c in indegree:
            if indegree[c] == 0:
                q.append(c)
        output = ""

        while q:
            curr = q.popleft()
            output += curr

            for nei in adj[curr]:
                indegree[nei] -= 1
                # adj[curr].remove(nei)
                if indegree[nei] == 0:
                    q.append(nei)


        if len(output) != len(indegree.keys()):
            return ""
        return output
            