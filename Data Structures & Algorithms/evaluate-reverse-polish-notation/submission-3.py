class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for t in tokens:
            if t == "+":
                b = int(stack.pop())
                a = int(stack.pop())
                cur = a + b
                stack.append(cur)
            elif t == "-":
                b = int(stack.pop())
                a = int(stack.pop())
                cur = a - b
                stack.append(cur)
            elif t == "*":
                b = int(stack.pop())
                a = int(stack.pop())
                cur = a * b
                stack.append(cur)
            elif t == "/":
                b = int(stack.pop())
                a = int(stack.pop())
                cur = a / b
                stack.append(int(cur))
            else:
                stack.append(t)
        return int(stack[-1])


        