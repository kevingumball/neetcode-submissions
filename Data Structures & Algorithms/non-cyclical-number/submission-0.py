class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        cur = 0
        while cur != 1:
            cur = 0
            for num in str(n):
                cur += int(num) ** 2
            n = cur
            if cur in seen:
                return False
            seen.add(cur)
        return True
        