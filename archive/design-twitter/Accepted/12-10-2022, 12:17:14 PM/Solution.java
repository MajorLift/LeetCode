// https://leetcode.com/problems/design-twitter

class Tweet {
    public int tweetId;
    public int timestamp;
    public Tweet next;

    public Tweet(int tweetId, int timestamp, Tweet next) {
        this.tweetId = tweetId;
        this.timestamp = timestamp;
        this.next = next;
    }
}

class User {
    private int userId;
    public Set<Integer> following;
    private Tweet latestTweet;
    public Tweet ptr;

    public User(int userId, HashSet<Integer> following, Tweet latestTweet) {
        this.userId = userId;
        this.following = following;
        this.latestTweet = latestTweet;
        this.ptr = this.latestTweet;
    }

    public void follow(int followeeId) {
        this.following.add(followeeId);
    }

    public void unfollow(int followeeId) {
        if (this.following.contains(followeeId)) this.following.remove(followeeId);
    }

    public void postTweet(Tweet tweet) {
        if (this.latestTweet != null) tweet.next = this.latestTweet;
        this.latestTweet = tweet;
        this.ptr = this.latestTweet;
    }

    public void incPtr() {
        this.ptr = this.ptr.next;
    }

    public void resetPtr() {
        this.ptr = this.latestTweet;
    }

    public boolean isEmpty() {
        return this.latestTweet == null;
    }
}

class UserComparator implements Comparator<User> {
    public int compare(User u1, User u2) {
        if (u1.ptr == null || u2.ptr == null) return 0;
        return u2.ptr.timestamp - u1.ptr.timestamp;
    }
}

class Twitter {
    private int clock;
    private Map<Integer, User> users;

    public Twitter() {
        this.clock = 0;
        this.users = new HashMap<>();
    }
    
    public void postTweet(int userId, int tweetId) {
        Tweet newTweet = new Tweet(tweetId, this.clock++, null);
        this.users.putIfAbsent(userId, new User(userId, new HashSet<>(Arrays.asList(userId)), null));
        this.users.get(userId).postTweet(newTweet);
    }
    
    public List<Integer> getNewsFeed(int userId) {
        if (!this.users.containsKey(userId)) return new ArrayList<>();
        for (int followeeId : this.users.get(userId).following) {
            if (this.users.containsKey(followeeId)) this.users.get(followeeId).resetPtr();
        }

        Queue<User> pq = new PriorityQueue<User>(new UserComparator());
        for (int followeeId : this.users.get(userId).following) {
            if (this.users.containsKey(followeeId) && !this.users.get(followeeId).isEmpty()) {
                pq.add(this.users.get(followeeId));
            }
        }

        List<Integer> feed = new ArrayList<>();
        while (!pq.isEmpty() && feed.size() < 10) {
            User user = pq.poll();
            feed.add(user.ptr.tweetId);
            if (user.ptr.next != null) {
                user.incPtr();
                pq.add(user);
            }
        }

        return feed;
    }
    
    public void follow(int followerId, int followeeId) {
        this.users.putIfAbsent(followerId, new User(followerId, new HashSet<>(Arrays.asList(followerId)), null));
        this.users.get(followerId).follow(followeeId);
    }
    
    public void unfollow(int followerId, int followeeId) {
        this.users.get(followerId).unfollow(followeeId);
    }
}


/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */