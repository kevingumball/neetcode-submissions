class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = {i:[] for i in range(n+1)}
    
        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            for nei in adj[i]:
                if nei == prev:
                    continue
                else:
                    if not dfs(nei, i):
                        return False
            return True
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            visit = set()
            if not dfs(n1, -1):
                return [n1, n2]
        
        return []
        