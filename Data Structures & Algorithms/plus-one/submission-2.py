class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        ans = []
        for dig in digits:
            res *= 10
            res += dig
        res += 1
        
        return [int(s) for s in str(res)]
        