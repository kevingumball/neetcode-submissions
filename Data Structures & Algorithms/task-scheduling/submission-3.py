from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        store = defaultdict(int)
        for ch in tasks:
            store[ch] += 1
        ava = []
        for ch, cnt in store.items():
            heapq.heappush(ava, (-cnt, ch))
        slp = []
        t = 0
        while ava or slp:
            while slp and slp[0][0] <= t:
                time, neg_cnt, ch = heapq.heappop(slp)
                heapq.heappush(ava, (neg_cnt, ch))
            if not ava:
                t = slp[0][0]
                continue
            neg_cnt, ch = heapq.heappop(ava)
            neg_cnt += 1
            if neg_cnt == 0:
                t += 1
                continue
            
            heapq.heappush(slp, (t + n + 1, neg_cnt, ch))
            t += 1

        return t 

        