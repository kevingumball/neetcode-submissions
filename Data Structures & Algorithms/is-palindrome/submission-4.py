class Solution:
    def isPalindrome(self, s: str) -> bool:
        cur = ""
        for c in s:
            if c.isalnum():
                cur += c.lower()
        l, r = 0, len(cur) - 1
        while l < r:
            if cur[l] != cur[r]:
                return False
            l += 1
            r -= 1
        return True
        