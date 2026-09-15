class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges = collections.defaultdict(list)
        tickets = sorted(tickets)[::-1]

        for com, des in tickets:
            edges[com].append(des)
        res = []
        def dfs(sor):
            while edges[sor]:
                des = edges[sor].pop()
                dfs(des)
            res.append(sor)

        dfs("JFK")
        return res[::-1]

        