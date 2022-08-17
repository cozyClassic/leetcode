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
    results = new Set()
    
    for (const word of words) {
        let result = []
        for (const w of word) {
            result[result.length] = hashs[w]
        }
        results.add(result.join(""))
    }
    return results.size
};