import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            dis = (math.sqrt((x)**2 + (y)**2))
            heapq.heappush(minheap, (dis, x, y))
        res = []
        for i in range(k):
            dis, x, y = heapq.heappop(minheap)
            res.append([x, y])
        return res
        