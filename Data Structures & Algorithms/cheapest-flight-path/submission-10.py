class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = {i:[] for i in range(n)}
        for com, des, pri in flights:
            edges[com].append((des, pri))
        
        visit = set()
        minheap = [(0, src, 0)]

        while minheap:
            cost1, com, stop = heapq.heappop(minheap)
            if com == dst and stop <= k + 1:
                return cost1
            if stop > k + 1:
                continue
            if (com, stop) in visit:
                continue
            visit.add((com, stop))
            for nei, cost2 in edges[com]:
                if (nei, stop + 1) not in visit:
                    heapq.heappush(minheap, (cost1 + cost2, nei, stop + 1))
        return -1
        