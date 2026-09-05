class Twitter:

    def __init__(self):

        self.tweet = defaultdict(list) #storing follow and unfollow
        self.follower = defaultdict(set)
        self.time = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([self.time, tweetId])
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        users = set(self.follower[userId])
        users.add(userId)
        
        for user in users:
            for time, tweetId in self.tweet[user]:
                heapq.heappush(heap,[-time, tweetId])

        res = []
        while heap and len(res) < 10:
            time, tweetId = heapq.heappop(heap)
            res.append(tweetId)

        return res
        #no followers

        #if he has folllowers
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)


         

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)
        

        
