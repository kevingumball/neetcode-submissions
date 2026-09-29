class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        q = deque()
        cnt = 0
        res = 0
        for c in s:
            if c in store:
                while q:
                    let = q.popleft()
                    store.remove(let)
                    cnt -= 1
                    if c == let:
                        break
            store.add(c)
            q.append(c)
            cnt += 1
            res = max(res, cnt)
        return res


        