class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        curmax = 0

        for num in nums:
            if curmax < 0:
                curmax = 0
            curmax += num
            maxsub = max(maxsub, curmax)
        return maxsub
        