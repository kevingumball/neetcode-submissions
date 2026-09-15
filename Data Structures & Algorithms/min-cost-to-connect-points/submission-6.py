class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = collections.defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                edges[i].append((abs(x1-x2)+abs(y1-y2), j))
                edges[j].append((abs(x1-x2)+abs(y1-y2), i))
        minHeap = [(0, 0)]
        res = 0
        visit = set()
        while minHeap:
            if len(visit) == len(points):
                break
            cost1, node1 = heapq.heappop(minHeap)
            if node1 in visit:
                continue
            res += cost1
            visit.add(node1)
            for cost2, node2 in edges[node1]:
                if node2 not in visit:
                    heapq.heappush(minHeap, (cost2, node2))
        return res

        