class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = defaultdict(list)
        for com, des, pri in flights:
            edges[com].append((des, pri))
        
        minheap = [(0, src, 0)]
        visit = set()

        while minheap:
            pri1, n1, stop = heapq.heappop(minheap)
            if n1 == dst and stop <= k + 1:
                return pri1
            if stop > k + 1:
                continue
            if n1 in visit:
                continue
            visit.add((n1, stop))
            for des, pri2 in edges[n1]:
                if (des, stop + 1) not in visit:
                    heapq.heappush(minheap, (pri1 + pri2, des, stop + 1))
                
        return -1


        