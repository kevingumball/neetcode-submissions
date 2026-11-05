class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache1 = [-1] * len(nums)
        cache2 = [-1] * len(nums)
        nums1 = nums[:-1]
        nums2 = nums[1:]

        def dfs(i):
            if i >= len(nums1):
                return 0
            if cache1[i] != -1:
                return cache1[i]
            cache1[i] = max(nums1[i] + dfs(i + 2), dfs(i + 1))
            return cache1[i]
        ans1 = dfs(0)

        def dfs2(i):
            if i >= len(nums2):
                return 0
            if cache2[i] != -1:
                return cache2[i]
            cache2[i] = max(nums2[i] + dfs2(i + 2), dfs2(i + 1))
            return cache2[i]
        ans2 = dfs2(0)
        return max(ans1, ans2)


        
        