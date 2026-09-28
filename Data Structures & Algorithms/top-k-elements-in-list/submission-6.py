class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)
        for num in nums:
            store[num] += 1
        tmp = []
        for ch, cnt in store.items():
            tmp.append([cnt, ch])
        tmp.sort()
        
        res = []
        for i in range(k):
            res.append(tmp.pop()[1])
        return res
        