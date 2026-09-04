class UnionFind:
    # need parent and rank
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, num):
        while num != self.parent[num]:
            self.parent[num] = self.parent[self.parent[num]]
            num = self.parent[num]
        return num
    
    def union(self, num1, num2):
        par1, par2 = self.find(num1), self.find(num2)
        if self.rank[par1] > self.rank[par2]:
            self.parent[par2] = par1
            self.rank[par1] += self.rank[par2]
        else:
            self.parent[par1] = par2
            self.rank[par2] += self.rank[par1]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToIndex = defaultdict(int)
        IndexToEmails = defaultdict(set)

        # match each email to a unique index
        for i, arr in enumerate(accounts):
            for j in range(1, len(arr)):
                email = arr[j]
                if email in emailToIndex:
                    uf.union(emailToIndex[email], i)
                else:
                    emailToIndex[email] = i
        
        # map each index to it's corresponding group of emails
        for i, arr in enumerate(accounts):
            for j in range(1, len(arr)):
                email = arr[j]
                parent = uf.find(i)
                IndexToEmails[parent].add(email)
        
        # return final array
        res = []
        for key, val in IndexToEmails.items():
            name = accounts[key][0]
            res.append([name] + sorted(val))
        return res