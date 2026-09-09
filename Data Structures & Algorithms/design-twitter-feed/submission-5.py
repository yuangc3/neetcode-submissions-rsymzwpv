class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet = defaultdict(list)
        self.follower = defaultdict(set)

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
        while heap and len(res) < 10:
            time, tweetId = heapq.heappop(heap)
            res.append(tweetId)
        
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)
