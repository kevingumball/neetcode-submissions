class MinStack:

    def __init__(self):
        self.stack = []
        self.ministack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.ministack and self.ministack[-1] < val:
            self.ministack.append(self.ministack[-1])
        else:
            self.ministack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.ministack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.ministack[-1]
