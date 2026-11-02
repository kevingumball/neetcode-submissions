class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        store = defaultdict(list)
        wordList.append(beginWord)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                store[pattern].append(word)
        
        q = deque()
        q.append(beginWord)
        visit = set()
        visit.add(beginWord)
        cnt = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return cnt
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in store[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            cnt += 1
        return 0