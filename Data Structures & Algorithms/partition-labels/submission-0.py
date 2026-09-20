class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, v in enumerate(s):
            lastIndex[v] = i
        
        size = 0
        cur, end = 0, 0
        res = []

        for i, t in enumerate(s):
            size += 1
            end = max(end, lastIndex[t])
            if i == end:
                res.append(size)
                size = 0
        return res
        