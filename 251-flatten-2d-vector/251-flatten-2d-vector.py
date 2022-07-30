class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.V = []
        for ve in vec:
            self.V.extend(ve)
        self.P = -1
        return

    def next(self) -> int:
        self.P += 1
        return self.V[self.P]

    def hasNext(self) -> bool:
        return self.P < len(self.V) - 1


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()