class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        store = {}
        for word in words:
            for ch in word:
                if ch not in store:
                    store[ch] = set()
        
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            minlen = min(len(w1), len(w2))
            if w1[:minlen] == w2[:minlen] and len(w1) > len(w2):
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    store[w1[j]].add(w2[j])
                    break
        res = []
        cycle = set()
        visit = set()

        def dfs(ch):
            if ch in visit:
                return True
            if ch in cycle:
                return False
            cycle.add(ch)
            for nei in store[ch]:
                if not dfs(nei):
                    return False
            cycle.remove(ch)
            visit.add(ch)
            res.append(ch)
            return True
        
        for ch in store.keys():
            if not dfs(ch):
                return ""
        return "".join(res)[::-1]



        