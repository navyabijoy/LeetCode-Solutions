class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.followMap[userId] # helps get the users the user follows
        minHeap = []
        res = []
        self.followMap[userId].add(userId)
        for followeeId in users:
            if followeeId in self.tweets: # if the user has posted tweets
                last = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][last]
                heapq.heappush(minHeap, (time, tweetId, followeeId, last - 1))

        while minHeap and len(res) < 10:
            time, tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId) # the final answer
            if idx >= 0:
                time, tweetId = self.tweets[followeeId][idx]
                heapq.heappush(minHeap, (time, tweetId, followeeId, idx - 1))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)