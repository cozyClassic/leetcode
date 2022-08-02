import sys
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        small_elements = dict() # (x,y) : value
        n = len(matrix)
        
        small_elements[(0,0)] = matrix[0][0]
        visited = [[False] * n for _ in range(n)]
        
        def pop_smallest_element(small_elements):
            min_value = sys.maxsize
            small_coords = (-1,-1)
            for coords, value in small_elements.items():
                if value < min_value :
                    min_value = value
                    small_coords = coords
            
            del(small_elements[small_coords])
            x,y = small_coords
            visited[x][y] = True
            
            return small_elements, small_coords
    
        for i in range(k):
            small_elements, coords = pop_smallest_element(small_elements)
            x, y = coords
            if x < n - 1 and not visited[x+1][y]:
                small_elements[(x+1,y)] = matrix[x+1][y]
            if y < n - 1 and not visited[x][y+1]:
                small_elements[(x,y+1)] = matrix[x][y+1]
        
        return matrix[x][y]
    
# 1. [0][0]이 0번째 최소값임
# 2. [0][1] 또는 [1][0]이 1번째 최소값임
# 3. 더한 element에 (+1,0), (0,+1)의 좌표가 더해진 값이 다음 최소값임
