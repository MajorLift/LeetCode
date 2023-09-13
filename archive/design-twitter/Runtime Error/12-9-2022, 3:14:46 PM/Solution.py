// https://leetcode.com/problems/design-twitter

from collections import defaultdict, deque

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(deque)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = [userId] + list(self.follows[userId])
        ptrs = [0] * len(users)
        lens = [len(self.tweets[_id]) for _id in users]

        pq = [(self.tweets[user][ptr], idx, user) for idx, (user, ptr) in enumerate(zip(users, ptrs))]
        heapq.heapify(pq)

        feed = deque()
        while pq and len(feed) < 10:
            (time, tweetId), idx, user = heapq.heappop(pq)
            feed.appendleft(tweetId)
            ptrs[idx] += 1
            if ptrs[idx] >= lens[idx]:
                continue
            heapq.heappush(pq, self.tweets[user][ptrs[idx]])
        return feed

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