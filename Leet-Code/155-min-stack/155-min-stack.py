#풀이 1 (Stack)
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if (len(self.stack) > 1):
            if self.min[-1] >= value:
                self.min.append(self.stack[-1])
            else:
                pass
        else:
            self.min.append(self.stack[-1])

        

    def pop(self) -> None:
        value = self.stack.pop()
        if self.min[-1] == value:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
