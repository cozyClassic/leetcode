class Solution {
    public int maxProfit(int[] prices) {
        int currMin = prices[0];
        int currRes = 0;
        for (int i=0; i<prices.length; i++) {
            currMin = Math.min(currMin, prices[i]);
            currRes = Math.max(currRes, prices[i] - currMin);
        }
        return currRes;
    }
}