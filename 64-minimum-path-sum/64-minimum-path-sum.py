class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = [[0]*n for _ in range(m)]
        
        
        for i in range(m) :
            for j in range(n) :
                if i == 0 and j == 0 :
                    result[i][j] = grid[0][0]
                    continue
                top = result[i-1][j] if i > 0 else 100*200
                left = result[i][j-1] if j > 0 else 100*200
                result[i][j] = min(top,left) + grid[i][j]
        
        return result[-1][-1]