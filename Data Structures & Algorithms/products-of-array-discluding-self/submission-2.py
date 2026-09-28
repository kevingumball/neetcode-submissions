class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front, back = [1] * len(nums), [1] * len(nums)
        res = []
        cur = 1
        for i in range(1, len(nums)):
            cur *= nums[i-1]
            front[i] = cur
        cur = 1
        for i in range(len(nums) - 2, -1, -1):
            cur *= nums[i + 1]
            back[i] = cur
        for i in range(len(nums)):
            res.append(front[i] * back[i])
        return res
        