class Solution:
    def minWindow(self, s: str, t: str) -> str:
        store1 = defaultdict(int)
        store2 = defaultdict(int)

        for c in t:
            store1[c] += 1
        need = len(store1)
        have = 0
        res = [-1, -1]
        maxlength = float("inf")
        l = 0

        for r in range(len(s)):
            
            store2[s[r]] += 1
            if s[r] in store1 and store2[s[r]] == store1[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < maxlength:
                    maxlength = r - l + 1
                    res = [l, r]
                store2[s[l]] -= 1                
                if store2[s[l]] + 1 == store1[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if maxlength != float("inf") else ""

        