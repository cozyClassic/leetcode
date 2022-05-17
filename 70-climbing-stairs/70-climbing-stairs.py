class Solution:
    def climbStairs(self, n: int) -> int:
        results = [0]*(n+1)
        results[0] = 1
        results[1] = 2
        for i in range(2,n):
            results[i] = results[i-1] + results[i-2]
        
        return results[n-1]