class Solution:
    def climbStairs(self, n: int) -> int:
        results = [0]*(n+1)
        results[0] = 1
        results[1] = 2
        p_prev, prev = 1, 2
        
        for i in range(2,n):
            results[i] = prev + p_prev
            p_prev, prev = prev, results[i]
        
        return results[n-1]