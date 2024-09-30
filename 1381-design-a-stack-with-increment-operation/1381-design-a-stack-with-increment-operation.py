class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize: self.stack.append(x)

    def pop(self) -> int:
        try:
            return self.stack.pop()
        except:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.stack),k)):
            self.stack[i] += val
