class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        cur = 0
        for num in nums:
            if cur != num:
                return cur
            cur += 1
        return cur
        