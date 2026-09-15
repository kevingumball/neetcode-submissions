class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = collections.defaultdict(list)
        for i in range(len(points)):
            ax, ay = points[i]
            for j in range(i + 1, len(points)):
                bx, by = points[j]
                edges[i].append((abs(ax - bx) + abs(ay - by), j))
                edges[j].append((abs(ax - bx) + abs(ay - by), i))
        
        visit = set()
        length = 0
        minHeap = [(0, 0)]
        while minHeap:
            if len(visit) == len(points):
                break
            w1, node1 = heapq.heappop(minHeap)
            if node1 in visit:
                continue
            length += w1
            visit.add(node1)
            for w2, node2 in edges[node1]:
                if node2 not in visit:
                    heapq.heappush(minHeap, (w2, node2))
        return length
            
        

        
                
        