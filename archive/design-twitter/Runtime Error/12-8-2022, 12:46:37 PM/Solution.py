// https://leetcode.com/problems/design-twitter

from collections import defaultdict, deque

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(deque)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendLeft((tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = list(self.follows[userId]) + [userId]
        pnts = [0] * 
        
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)