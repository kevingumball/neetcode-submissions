class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)

        for i in range(n-1,-1,-1):
            res = 1
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    res = max(res,1 + dp[j])
            dp[i] = res
        return max(dp[i] for i in range(n))
