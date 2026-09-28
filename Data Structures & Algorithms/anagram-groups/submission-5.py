class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            store[sortedS].append(s)
        return list(store.values())
        