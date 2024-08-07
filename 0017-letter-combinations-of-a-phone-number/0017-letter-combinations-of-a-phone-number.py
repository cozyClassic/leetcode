from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits :
            return []
        
        dic = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl",
              "6" : "mon", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        args = [val for key,val in dic.items() if key in digits]
        return ["".join(a) for a in list(product(*args))]
    
     