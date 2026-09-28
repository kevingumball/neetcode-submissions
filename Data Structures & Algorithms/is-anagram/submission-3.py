class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store1 = {}
        store2 = {}
        for num in s:
            store1[num] = store1.get(num, 0) + 1
        for num in t:
            store2[num] = store2.get(num, 0) + 1
        return store1 == store2
        