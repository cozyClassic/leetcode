/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let result = ""
    let temp = []
    for (_s of s) {
        if (temp.includes(_s)) {
            if (temp.length > result.length){
                result = temp.join("")
            }
            while (temp.includes(_s)) {
                temp.shift()
            }
            temp[temp.length] = _s
        } else {
            temp[temp.length] = _s
        }
    }
    if (temp.length > result.length) {
        return temp.length
    }
    return result.length
};