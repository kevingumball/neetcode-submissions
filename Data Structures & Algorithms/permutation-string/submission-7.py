class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        store1 = defaultdict(int)
        for c in s1:
            store1[c] += 1
        store2 = defaultdict(int)
        l = 0

        for r in range(len(s2)):
            store2[s2[r]] += 1

            if r - l == len(s1):
                store2[s2[l]] -= 1
                if store2[s2[l]] == 0:
                    del store2[s2[l]]
                l += 1
            if store1 == store2:
                return True
        return False

        