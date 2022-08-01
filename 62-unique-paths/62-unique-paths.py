class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        # init
        paths = [[0]*n for _ in range(m)]
        paths[0][1] = 1
        paths[1][0] = 1
        
        for i in range(m):
            for j in range(n):
                if i >= 1 :
                    paths[i][j] += paths[i-1][j]
                if j >= 1 :
                    paths[i][j] += paths[i][j-1]
        
        return paths[-1][-1]