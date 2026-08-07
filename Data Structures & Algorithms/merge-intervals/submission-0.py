class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curint = intervals[0]
        res = []

        for i in range(1,len(intervals)):
            if curint[1] < intervals[i][0]:
                res.append(curint)
                curint = intervals[i]
            else:
                curint = [min(curint[0], intervals[i][0]), max(curint[1], intervals[i][1])]
                #if i == len(intervals)-1:
                    #res.append(curint)
        res.append(curint)
        return res