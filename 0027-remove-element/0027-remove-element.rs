impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut l: usize = 0;

        for r in 0..nums.len() {
            if (nums[r] != val) {
                nums[l] = nums[r];
                l += 1;
            }
        }

        return l as i32;
   }
}