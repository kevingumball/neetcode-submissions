class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                cost = abs(x1-x2) + abs(y1-y2)
                edges[i].append((j, cost))
                edges[j].append((i, cost))
        
        res = 0
        minheap = []
        minheap.append((0, 0))
        visit = set()

        while minheap:
            if len(visit) == len(points):
                break
            w1, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            res += w1
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap, (w2, n2))
        return res
                

        