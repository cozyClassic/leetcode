class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        k = 1
        while k < n:
            k *= 3
        
        return k == n