class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for n1, n2, t in times:
            edges[n1].append((n2, t))
        minheap = [(0, k)]
        res = 0
        visit = set()
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            res = max(res, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap, (w1 + w2, n2))
        
        return res if len(visit) == n else -1

        