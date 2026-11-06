class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = max(nums)
        curMax = 1
        curMin = 1

        for num in nums:
            tmp = curMax
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(curMin * num, tmp * num, num)
            largest = max(largest, curMax, curMin)
        return largest
        