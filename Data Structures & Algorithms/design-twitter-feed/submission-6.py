from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.flist = defaultdict(set)
        self.plist = defaultdict(list)
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.plist[userId].append((self.t, tweetId))
        self.t -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        self.flist[userId].add(userId)
        minheap = []
        res = []

        for followeeId in self.flist[userId]:
            idx = len(self.plist[followeeId])
            if idx:
                time, tweetId = self.plist[followeeId][idx - 1]
                heapq.heappush(minheap, (time, tweetId, followeeId, idx))
        while minheap and len(res) < 10:
            time, tweetId, followeeId, idx = heapq.heappop(minheap)
            res.append(tweetId)
            idx -= 1
            if idx != 0:
                time, tweetId = self.plist[followeeId][idx - 1]
                heapq.heappush(minheap, (time, tweetId, followeeId, idx))
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.flist[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.flist[followerId]:
            self.flist[followerId].remove(followeeId)
