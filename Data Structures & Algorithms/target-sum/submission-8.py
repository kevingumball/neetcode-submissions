class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            new_dp = defaultdict(int)
            for count, ways in dp.items():
                new_dp[count + num] += ways
                new_dp[count - num] += ways
            dp = new_dp
        return new_dp[target]