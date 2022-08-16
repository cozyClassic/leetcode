function twoSum(nums: number[], target: number): number[] {
    let hash:Object = {};
    let num:number = -1;
    for (let i=0; i<nums.length; i++){
        num = nums[i];
        if (hash[target-num] != undefined) {
            return [hash[target-num], i];
        }
        hash[num] = i;        
    }
};