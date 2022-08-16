function twoSum(nums: number[], target: number): number[] {
    // 원본 인덱스 유지하면서 sort하기
    let index_nums:object[] = [...nums.entries()]
    index_nums.sort((prev,next) => prev[1] - next[1]) 
    let left:number = 0
    let right:number = nums.length-1;
    
    while (left < right) {
        let l = index_nums[left]
        let r = index_nums[right]
        let sum:number = l[1] + r[1]
        if (sum == target){
            return [l[0], r[0]]
        } else if (sum < target) {
            left += 1;
        } else if (sum > target) {
            right -= 1;
        }
    }   
    return [1]
};