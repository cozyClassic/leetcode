class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        L = len(cost)
        totals = [0] * L
        totals[0] = cost[0]
        totals[1] = cost[1]
        
        for i in range(2,L):
            totals[i] = cost[i] + min(totals[i-1],totals[i-2])
        
        return min(totals[L-1],totals[L-2])