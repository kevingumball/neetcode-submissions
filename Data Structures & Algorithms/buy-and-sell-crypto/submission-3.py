class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0
        while r < len(prices):
            cur = prices[r] - prices[l]
            res = max(res, cur)
            if cur < 0:
                l = r
                r += 1
            else:
                r += 1
        return res
        