class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1:
            return min(1, citations[0])

        citations.sort(reverse=True)

        result = 0        

        for i in range(len(citations)):
            curr = min(i+1, citations[i])
            result = max(curr, result)
        
        return result