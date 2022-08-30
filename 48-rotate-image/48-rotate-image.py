class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        result = [[0] * n for _ in range(n)]
        
        for y in range(n) :
            for x in range(n) :
                result[x][n-1-y] = matrix[y][x]
        
        matrix[:] = result