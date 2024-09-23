class Solution:
    def str_to_gen(self, string):
        for char in string:
            yield char

    def isSubsequence(self, S: str, T: str) -> bool:
        if S == "": return True

        s_gen = self.str_to_gen(S)
        s = next(s_gen)

        try:
            for t in T:
                if t == s:
                    s = next(s_gen)
            return False
        except:
            return True