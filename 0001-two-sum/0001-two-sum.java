class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map = new HashMap<Integer, Integer>();
        for (Integer i=0; i< nums.length; i++) {
            Integer t = target-nums[i];
            if (map.containsKey(t)) {
                return new int[] {i, map.get(t)};
            } else {
                map.put(nums[i], i);
            }
        }
        return new int[]{0,0};
    }
}