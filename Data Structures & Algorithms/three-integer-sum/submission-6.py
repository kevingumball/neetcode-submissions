class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            if i - 1 >= 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                need = 0 - nums[i] - nums[l] - nums[r]
                if need == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif need < 0:
                    r -= 1
                else:
                    l += 1
        return res

        