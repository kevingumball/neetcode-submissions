class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for s in strs:
            alp = [0] * 26
            for c in s:
                alp[ord(c) - ord("a")] += 1
            store[tuple(alp)].append(s)
        return list(store.values())
                
        