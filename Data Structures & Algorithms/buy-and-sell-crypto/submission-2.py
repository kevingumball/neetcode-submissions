class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur, maxpro = 0, 0
        l = 0

        for r in range(1,len(prices)):
            cur = prices[r] - prices[l]
            maxpro = max(maxpro, cur)
            if prices[r] < prices[l]:
                l = r
        return maxpro