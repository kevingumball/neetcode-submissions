import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if self.small and self.big and -self.small[0] > self.big[0]:
            b = heapq.heappop(self.big)
            neg_s = heapq.heappop(self.small)
            heapq.heappush(self.small, -b)
            heapq.heappush(self.big, -neg_s)
        
        if len(self.small) > len(self.big) + 1:
            neg_s = heapq.heappop(self.small)
            heapq.heappush(self.big, -neg_s)


    def findMedian(self) -> float:
        if self.small and self.big:
            if len(self.small) > len(self.big):
                neg_num = self.small[0]
                return -neg_num
            else:
                neg_num = self.small[0]
                num2 = self.big[0]
                return (-neg_num + num2) / 2
        elif self.small:
            return -self.small[0]
        
        