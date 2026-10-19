import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []

        for st in stones:
            heapq.heappush(maxheap, -st)
        
        while maxheap and len(maxheap) > 1:
            st1 = -heapq.heappop(maxheap)
            st2 = -heapq.heappop(maxheap)
            remain = st1 - st2
            if remain != 0:
                heapq.heappush(maxheap, -remain)

        return -maxheap[0] if maxheap else 0
        