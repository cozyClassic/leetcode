class Solution:
    def dividePlayers(self, s: List[int]) -> int:
        if len(s) == 2: return s[0] * s[1]

        s.sort()
        r = 0
        d = s[0] + s[-1]
        L = len(s) - 1

        for i in range((L+1)//2):
            if s[i] + s[L-i] != d: return -1
            r += s[i] * s[L-i]

        return r