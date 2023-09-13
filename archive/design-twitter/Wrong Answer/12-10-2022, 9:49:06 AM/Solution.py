// https://leetcode.com/problems/design-twitter

class Tweet:
    def __init__(self, tweetId, timestamp, nextPtr=None):
        self.tweetId = tweetId
        self.timestamp = timestamp
        self.nextPtr = nextPtr

class User:
    def __init__(self, userId, follows=set(), latestTweet=None):
        self.userId = userId
        self.follows = follows
        if self.userId not in self.follows:
            self.follows.add(self.userId)
        self.latestTweet = latestTweet
        self.ptr = self.latestTweet

    def __lt__(self, other):
        return self.ptr.timestamp > other.ptr.timestamp

    def follow(self, followeeId):
        self.follows.add(followeeId)

    def unfollow(self, followeeId):
        self.follows.remove(followeeId)

    def postTweet(self, tweet):
        if self.latestTweet:
            tweet.nextPtr = self.latestTweet
        self.latestTweet = tweet
        self.ptr = self.latestTweet

    def incPtr(self):
        self.ptr = self.ptr.nextPtr

    def resetPtr(self):
        self.ptr = self.latestTweet

    def isEmpty(self):
        return self.latestTweet is None

class Twitter:
    def __init__(self):
        self.clock = 0
        self.users = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        newTweet = Tweet(tweetId, self.clock)
        if userId not in self.users:
            self.users[userId] = User(userId)
        self.users[userId].postTweet(newTweet)
        self.clock += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        pq = []
        for followeeId in self.users[userId].follows:
            if followeeId in self.users and not self.users[followeeId].isEmpty():
                pq.append(self.users[followeeId])
        heapq.heapify(pq)
        feed = []
        while pq and len(feed) < 10:
            user = heapq.heappop(pq)
            feed.append(user.ptr.tweetId)
            user.incPtr()
            if user.ptr:
                heapq.heappush(pq, user)

        for followeeId in self.users[userId].follows:
            if followeeId in self.users:
                self.users[followeeId].resetPtr()
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        self.users[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].unfollow(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)