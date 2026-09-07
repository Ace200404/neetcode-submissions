class Twitter:

    def __init__(self):
        self.count=0
        #tracks the user and followers
        self.followMap=defaultdict(set)
        #tracks the tween and count timer for the userid
        self.tweetMap=defaultdict(list)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count+=1

        self.tweetMap[userId].append([self.count,tweetId])


    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        maxHeap=[]
        self.followMap[userId].add(userId)

        for followers in self.followMap[userId]:
            if followers in self.tweetMap:
                for count, post in self.tweetMap[followers][-10:]:
                    maxHeap.append([-count,post])
        heapq.heapify(maxHeap)

        while maxHeap and len(res)<10:
            counter, postId=heapq.heappop(maxHeap)
            res.append(postId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.followMap[followerId].discard(followeeId)