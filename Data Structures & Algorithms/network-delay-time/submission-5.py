class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for n1, n2, t in times:
            edges[n1].append((n2, t))
        
        minheap = [(0, k)]
        visit = set()
        res = 0
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            res = max(res, w1)
            visit.add(n1)

            for nei, w2 in edges[n1]:
                if nei not in visit:
                    heapq.heappush(minheap, (w1 + w2, nei))
        return res if len(visit) == n else -1
        