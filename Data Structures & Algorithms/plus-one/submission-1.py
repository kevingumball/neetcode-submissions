class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        ans = []
        for dig in digits:
            res *= 10
            res += dig
        res += 1
        for s in str(res):
            ans.append(s)

        return ans
        