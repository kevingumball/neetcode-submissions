class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1, -1]
        length = float("inf")
        l = 0
        store1 = defaultdict(int)
        for let in t:
            store1[let] += 1
        need = len(store1)
        have = 0
        store2 = defaultdict(int)

        for r in range(len(s)):
            store2[s[r]] += 1
            if s[r] in store1 and store2[s[r]] == store1[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < length:
                    res = [l, r]
                    length = (r - l + 1)
                store2[s[l]] -= 1
                if store2[s[l]] + 1 == store1[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if length != float("inf") else ""

