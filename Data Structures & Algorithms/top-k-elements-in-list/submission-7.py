class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)
        for num in nums:
            store[num] += 1
        minHeap = []
        for v, cnt in store.items():
            heapq.heappush(minHeap, (-cnt, v))
        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res
        