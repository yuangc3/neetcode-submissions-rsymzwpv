class Twitter:

    def __init__(self):
        self.time = 0
        self.follower = defaultdict(set)
        self.tweet = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.follower[userId]
        users.add(userId)
        for user in users:
            for time, tweetId in self.tweet[user]:
                heapq.heappush(heap, (-time, tweetId))
        res = []
        for i in range(10):
            if not heap:
                break
            time, tweetId = heapq.heappop(heap)
            res.append(tweetId)
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)
