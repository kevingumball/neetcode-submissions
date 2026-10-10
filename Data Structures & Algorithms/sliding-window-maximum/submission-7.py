class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)
        minHeap = []
        for i in range(k):
            store[nums[i]] += 1
            heapq.heappush(minHeap, -nums[i])
        res = [-minHeap[0]]
        l = 0
        for r in range(k, len(nums)):
            store[nums[r]] += 1
            heapq.heappush(minHeap, -nums[r])
            store[nums[l]] -= 1
            if store[nums[l]] == 0:
                del store[nums[l]]
            while -minHeap[0] not in store:
                heapq.heappop(minHeap)
            l += 1
            res.append(-minHeap[0])
        return res

        

        