class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)

        def dfs(i):
            if i in dp:
                return dp[i]
            res = 1
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    res = max(res, 1 + dfs(j))
            
            dp[i] = res
            return dp[i]
        
        return max(dfs(i) for i in range(len(nums))) 
