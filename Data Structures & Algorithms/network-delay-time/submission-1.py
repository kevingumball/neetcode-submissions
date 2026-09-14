class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        visit = set()
        t = 0
        for u, v, t in times:
            edges[u].append((v, t))

        minHeap = [(0,k)]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            t = w1
            visit.add(n1)
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2,n2))
        return t if len(visit) == n else -1
            
        