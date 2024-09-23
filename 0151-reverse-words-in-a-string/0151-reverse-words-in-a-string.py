from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        Q = deque()
        for l in s.strip().split(" "):
            if l == "":
                continue
            Q.appendleft(l)
        return " ".join(Q)