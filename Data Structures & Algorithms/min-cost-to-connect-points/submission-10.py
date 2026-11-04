class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                dis = abs(x1 - x2) + abs(y1 - y2)
                edges[i].append((j, dis))
                edges[j].append((i, dis))
        
        minheap = [(0, 0)]
        res = 0
        visit = set()
        while minheap:
            if len(visit) == len(points):
                break
            cost, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            res += cost
            visit.add(n1)
            for n2, cost2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap, (cost2, n2))
        return res

        