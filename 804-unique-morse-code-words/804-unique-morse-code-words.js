/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function(words) {
    let m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."][Symbol.iterator]();
    let a = "abcdefghijklmnopqrstuvwxyz"[Symbol.iterator]();
    let hashs = {};
    
    for (let i=0; i<26; i++) {
        hashs[a.next().value] = m.next().value
    }
    results = new Set(words.map((word) => word.split("").map((char) => hashs[char]).join("")))
    return results.size
};