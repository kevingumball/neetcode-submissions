class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        maxsub = nums[0]

        for i in range(0, len(nums)):
            if cursum < 0:
                cursum = 0
            cursum += nums[i]
            maxsub = max(maxsub, cursum)
        return maxsub
        