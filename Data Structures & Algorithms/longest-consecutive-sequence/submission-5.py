class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)

        longest = 0
        for num in nums:
            if num - 1 in store:
                continue
            length = 1
            while num + 1 in store:
                num += 1
                length += 1
            longest = max(longest, length)
        return longest 
        