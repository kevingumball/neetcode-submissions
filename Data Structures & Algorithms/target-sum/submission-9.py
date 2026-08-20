class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}

        def dfs(i, cur):
            if i == n:
                if cur == target:
                    return 1
                return 0
            
            if (i, cur) in dp:
                return dp[(i, cur)]
            
            res = dfs(i + 1, cur + nums[i])
            res += dfs(i + 1, cur - nums[i])

            dp[(i, cur)] = res
            return res
        return dfs(0, 0)