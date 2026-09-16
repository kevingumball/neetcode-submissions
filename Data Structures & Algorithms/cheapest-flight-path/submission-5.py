class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for com, to, price in flights:
            edges[com].append((price, to))
        
        minHeap = [(0, src, 0)]
        visit = set()
        res = 0
        

        while minHeap:
            cost1, plc1, t = heapq.heappop(minHeap)
            if t - 1 > k:
                continue
            if (plc1, t) in visit:
                continue
            visit.add((plc1, t))
            if plc1 == dst:
                return cost1
            for cost2, plc2 in edges[plc1]:
                if (plc2, t + 1) not in visit:
                    heapq.heappush(minHeap, (cost1 + cost2, plc2, t + 1))
        return -1


        