class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
        
        res = 1
        
        prev = heapq.heappop(minHeap)
        cur = 1
        while minHeap:
            num = heapq.heappop(minHeap)
            if num == prev:
                continue
            if num - 1 != prev:
                prev = num
                cur = 1
                continue
            cur += 1
            prev = num
            res = max(res, cur)
        return res
        