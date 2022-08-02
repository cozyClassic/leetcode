import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        all_lists = []
        
        for m in matrix:
            all_lists.extend(m)
        
        heapq.heapify(all_lists)
        kth_element = 0
        for i in range(k):
            kth_element = heapq.heappop(all_lists)
        return kth_element