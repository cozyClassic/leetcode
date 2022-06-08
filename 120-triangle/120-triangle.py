class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        results = triangle[:]
        
        for i in range(len(triangle)) :
            curr = results[i]
            if i == 0 : 
                prev = curr
                continue
            L = len(triangle[i])
            
            for j in range(L):
                if j == 0 :
                    curr[j] += prev[0]
                elif j == L-1 :
                    curr[j] += prev[j-1]
                else :
                    curr[j] += min(prev[j-1],prev[j])
            prev = curr
        return min(results[-1])