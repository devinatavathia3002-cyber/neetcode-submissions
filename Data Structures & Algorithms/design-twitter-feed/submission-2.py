class Twitter:

    def __init__(self):
        self.followers = defaultdict(set) # map user --> [followers]
        self.users = defaultdict(list) # map user --> ([time, tweet])
        self.time = 0 # time
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followers[userId].add(userId)

        res = []
        minHeap = []

        for follower in self.followers[userId]:
            if self.users[follower]:
                index = len(self.users[follower]) - 1
                time, tweet = self.users[follower][index]
                heapq.heappush(minHeap, [time, tweet, follower, index - 1])
        
        while minHeap and len(res) < 10:
            time, tweet, follower, index = heapq.heappop(minHeap)
            res.append(tweet)
            if index >= 0:
                time, tweet = self.users[follower][index]
                heapq.heappush(minHeap, [time, tweet, follower, index - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
