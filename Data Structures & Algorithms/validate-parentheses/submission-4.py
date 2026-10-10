class Solution:
    def isValid(self, s: str) -> bool:
        store = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for c in s:
            if c in store:
                if stack and stack[-1] == store[c]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(c)
        return True if not stack else False

        