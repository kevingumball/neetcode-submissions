class Solution:
    def reverse(self, x: int) -> int:
        org = x
        x = abs(x)
        x = int(str(x)[::-1])

        if org < 0:
            x *= -1
        if x < -(1 << 31) or x > (1 << 31) - 1:
            return 0
        return x
        