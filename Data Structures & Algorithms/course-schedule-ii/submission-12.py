class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}

        for cor, pre in prerequisites:
            preMap[cor].append(pre)
        
        res = []
        visit = set()
        already = set()

        def dfs(cor):
            if cor in visit:
                return False
            if preMap[cor] == []:
                if cor not in already:
                    res.append(cor)
                    already.add(cor)
                return True
            visit.add(cor)
            for pre in preMap[cor]:
                if not dfs(pre):
                    return False
            visit.remove(cor)
            preMap[cor] = []
            res.append(cor)
            already.add(cor)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res



        