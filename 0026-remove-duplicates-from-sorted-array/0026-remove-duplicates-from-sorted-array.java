class Solution {
    public int removeDuplicates(int[] nums) {
        int l = 0;
        for (int r=1; r< nums.length; r++) {
            if (nums[l] == nums[r]) {
                nums[r] = 101;
                continue;
            }
            l += 1;
            nums[l] = nums[r];
		}
        return l+1;
    }
}