class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache1 = [-1] * len(nums)
        cache2 = [-1] * len(nums)
        nums1 = nums[:-1]
        nums2 = nums[1:]

        def dfs(i, nums, cache):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = max(nums[i] + dfs(i + 2, nums, cache), dfs(i + 1, nums, cache))
            return cache[i]
        return max(dfs(0, nums1, cache1), dfs(0, nums2, cache2))

        
        
        