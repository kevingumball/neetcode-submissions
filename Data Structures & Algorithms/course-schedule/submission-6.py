class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for cor, pre in prerequisites:
            preMap[cor].append(pre)
        
        cycle = set()
        visit = set()

        def dfs(cor):
            if cor in visit:
                return True
            if cor in cycle:
                return False
            cycle.add(cor)
            for pre in preMap[cor]:
                if not dfs(pre):
                    return False
            cycle.remove(cor)
            visit.add(cor)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True       