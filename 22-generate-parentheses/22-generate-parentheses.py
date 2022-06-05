class Solution:
    results = []
    DICT = {"(":1, ")":-1}
    N = 0
    def generateParenthesis(self, n: int) -> List[str]:
        self.N = n
        self.results = []
        self.gen("" ,0,0)

        return self.results

    def gen(self, result, left, right):
        if left + right == self.N*2 :
            self.results.append(result)
            return
        
        if left < self.N:
            self.gen(result+"(", left+1, right)
        
        if left > right :
            self.gen(result+")", left, right+1)
        
        return