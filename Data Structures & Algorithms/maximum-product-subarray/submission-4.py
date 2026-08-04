class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        MaxPro = max(nums)
        curMin = 1
        curMax = 1

        for num in nums:
            tempMax = curMax
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(curMin * num, tempMax * num, num)
            MaxPro = max(MaxPro, curMax, curMin)
        return MaxPro