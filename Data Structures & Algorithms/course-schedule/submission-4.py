class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for cor, pre in prerequisites:
            preMap[cor].append(pre)
        
        visit = set()

        def dfs(cor):
            if cor in visit:
                return False
            if preMap[cor] == []:
                return True
            
            visit.add(cor)
            for pre in preMap[cor]:
                if not dfs(pre):
                    return False
            visit.remove(cor)
            preMap[cor] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        