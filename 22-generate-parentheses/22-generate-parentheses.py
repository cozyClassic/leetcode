class Solution:
    results = []
    DICT = {"(":1, ")":-1}
    N = 0
    def generateParenthesis(self, n: int) -> List[str]:
        self.N = n
        self.results = []
        self.gen("")        
        
        return self.results

    def gen(self, result):
        if len(result) == self.N*2 :
            self.results.append(result)
            return
        
        count = 0
        for r in result:
            count += self.DICT[r]
        if count == 0 :
            self.gen(result+"(")
        else :
            self.gen(result+")")
            if result.count("(") < self.N:
                self.gen(result+"(")
        return