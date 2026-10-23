class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse = True)
        res = []
        cur = []

        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates):
                return 
            if total > target:
                return 
            
            cur.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res
        