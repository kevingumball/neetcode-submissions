class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse = True)
        i = 0
        total = 0
        cur = []
        res = []
        
        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return 
            if total > target or i >= len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i+1, total + candidates[i])
            cur.pop()

            while i < len(candidates)-1 and candidates[i+1] == candidates[i]:
                i += 1

            dfs(i+1, total)
                    
        dfs(0, 0)
        return res

        