class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        store = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        
        for c in s:
            if c in store:
                if stack and store[c] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False
            
            stack.append(c)
        return True if not stack else False