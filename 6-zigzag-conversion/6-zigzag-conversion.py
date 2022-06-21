from collections import deque
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        S = deque(s)
        columns = 0
        N = numRows - 2
        while S :
            if columns == 0 :
                columns = N
                for row in rows :
                    row.append(S.popleft())
                    if not S :
                        break
            else :
                rows[columns].append(S.popleft())
                columns -= 1
        
        result = ""
        for row in rows :
            result += "".join(row)

        return result
        