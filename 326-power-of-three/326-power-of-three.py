class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0 :
            return False
        
        while n > 1:
            n,last = divmod(n,3)
            if last != 0 :
                return False
        
        return n == 1