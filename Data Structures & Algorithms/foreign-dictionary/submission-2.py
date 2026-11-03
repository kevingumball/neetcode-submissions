class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for w in words:
            for ch in w:
                if ch not in adj:
                    adj[ch] = set()
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = set()
        cycle = set()
        res = []

        def dfs(ch):
            if ch in cycle:
                return False
            if ch in visit:
                return True
            cycle.add(ch)
            for nei in adj[ch]:
                if not dfs(nei):
                    return False
            cycle.remove(ch)
            visit.add(ch)
            res.append(ch)
            return True

        for ch in adj.keys():
            if not dfs(ch):
                return ""
        return "".join(res)[::-1]

        