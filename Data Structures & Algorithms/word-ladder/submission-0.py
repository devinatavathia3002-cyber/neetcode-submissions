class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        visit = set()
        q = deque()
        adj = defaultdict(list)
        layer = 0

        for word in wordList:
            for letter in range(len(word)):
                key = word[:letter] + "*" + word[letter + 1:]
                adj[key].append(word)
        
        # initialize queue
        for letter in range(len(beginWord)):
            key = beginWord[:letter] + "*" + beginWord[letter + 1:]
            q.append(key)
        
        while q:
            length = len(q)
            layer += 1 # layer increment
            for i in range(length):
                pattern = q.popleft()
                visit.add(pattern) # visit tracker
                for index, word in enumerate(adj[pattern]):
                    if word == endWord:
                        return layer + 1
                    for letter in range(len(word)):
                        key = word[:letter] + "*" + word[letter + 1:]
                        if key not in visit:
                            q.append(key)
                    
        return 0