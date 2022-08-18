/**
 * @param {number[]} arr
 * @return {number}
 */
function counter(arr) {
    let hashs = {};
    for (num of arr){
        if (num in hashs) {
            hashs[num] += 1;
        } else {
            hashs[num] = 1;
        }
    }
    return hashs;
};

var minSetSize = function(arr) {
    let hashs = counter(arr);
    let keys = Object.keys(hashs);
    keys.sort((curr_key, other_key) => (hashs[other_key] - hashs[curr_key]))
    let goal = (arr.length/2).toFixed(0);
    let result = 0;
    for (let key of keys){
        result += 1;
        goal -= hashs[key];
        if (goal <= 0) {
            break;
        }
    }
    return result;
};