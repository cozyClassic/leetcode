class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = {x:1 for x in arr}
        
        for i in range(len(arr)):
            for j in range(i):
                curr = arr[i]
                prev1 = arr[j]
                if curr/prev1 in dp:
                    prev2 = arr[i]//arr[j]
                    dp[curr] += dp[prev1] * dp[prev2]
        return sum(dp[x] for x in dp) % (10**9+7)