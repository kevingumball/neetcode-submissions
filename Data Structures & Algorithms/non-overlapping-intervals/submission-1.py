class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        lastEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if lastEnd <= start:
                lastEnd = end
                continue
            else:
                res += 1
                lastEnd = min(lastEnd, end)
        
        return res