class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.increments = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize: 
            self.stack.append(x)
            self.increments.append(0)

    def pop(self) -> int:
        try:
            return self.stack.pop() + self.increments.pop()
        except:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.increments),k)):
            self.increments[i] += val
