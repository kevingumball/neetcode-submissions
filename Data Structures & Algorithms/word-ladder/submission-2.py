class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        nei = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i+1:]
                nei[pattern].append(w)
        
        q = deque()
        q.append(beginWord)
        res = 1
        visit = set()

        while q:
            for i in range(len(q)):
                word = q.popleft()
                visit.add(word)
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for w in nei[pattern]:
                        if w not in visit:
                            q.append(w)
            res += 1
        return 0



        