class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        
        return a if a < max_int else ~(a ^ mask)
        