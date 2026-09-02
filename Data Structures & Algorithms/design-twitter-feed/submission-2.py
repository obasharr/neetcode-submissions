class Tweet:
    def __init__(self, tweet_id: int, time: int):
        self.id = tweet_id 
        self.time = time
        self.next = None

class User:
    def __init__(self, user_id: int):
        self.id = user_id
        self.followed = set()
        self.follow(user_id)
        self.tweet_head = None
    
    def follow(self, user_id: int):
        self.followed.add(user_id)
    
    def unfollow(self, user_id: int):
        if user_id != self.id:
            self.followed.discard(user_id)
    
    def post(self, tweet_id: int, time: int):
        tweet = Tweet(tweet_id, time)
        tweet.next = self.tweet_head
        self.tweet_head = tweet

class Twitter:

    def __init__(self):
        self.time = 0
        self.user_map = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_map:
            self.user_map[userId] = User(userId)
        self.user_map[userId].post(tweetId, self.time)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = []

        if userId not in self.user_map:
            return news_feed
        
        max_heap = []

        for user in self.user_map[userId].followed:
            tweet = self.user_map[user].tweet_head
            if tweet:
               heapq.heappush(max_heap, (-tweet.time, tweet.id, tweet))

        while max_heap and len(news_feed) < 10:
            _, _, tweet = heapq.heappop(max_heap)
            news_feed.append(tweet.id)

            if tweet.next:
                heapq.heappush(max_heap, (-tweet.next.time, tweet.next.id, tweet.next))
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_map:
            self.user_map[followerId] = User(followerId)
        
        if followeeId not in self.user_map:
            self.user_map[followeeId] = User(followeeId)

        self.user_map[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_map:
            self.user_map[followerId].unfollow(followeeId)





