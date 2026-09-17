class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #dfs
        n = len(nums)
        dp = {}
        def dfs(i):
            if i >= n - 1:
                return True
            if i in dp:
                return dp[i]
            dp[i] = False
            for j in range(1, nums[i] + 1):
                if dfs(i + j):
                    dp[i] = True
                    break
            return dp[i]
                        
        return dfs(0)
            



        