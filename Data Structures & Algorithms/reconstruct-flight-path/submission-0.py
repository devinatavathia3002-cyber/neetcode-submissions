class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = defaultdict(list)
        tickets.sort()

        for ticket in tickets:
            src, dest = ticket
            adj[src].append(dest)
        
        res = ["JFK"]

        def dfs(source):
            nonlocal res
            temp = adj[source].copy()
            if len(res) == len(tickets) + 1:
                return True
            if len(temp) == 0:
                return False
            
            for i, dest in enumerate(temp):
                adj[source].pop(i)
                res.append(dest)
                if dfs(dest):
                    return True
                # backtrack
                adj[source].insert(i, dest)
                res.pop()
            return False
            

        dfs("JFK")
        return res
        