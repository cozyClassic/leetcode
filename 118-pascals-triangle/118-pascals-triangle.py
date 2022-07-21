class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        if numRows == 1 :
            return result
        
        for i in range(1,numRows):
            prev_row = result[-1]
            this_row = prev_row[:]
            
            for j in range(1,len(prev_row)):
                this_row[j] += prev_row[j-1]
                
            this_row.append(prev_row[-1])
            result.append(this_row)
        return result

s = Solution()