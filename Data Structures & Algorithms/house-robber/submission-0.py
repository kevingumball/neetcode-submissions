class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        n = len(nums)
        for i in range(len(nums)):
            nums[i] = max(rob1 + nums[i],rob2)
            rob1 = rob2
            rob2 = nums[i]
        return nums[n-1]