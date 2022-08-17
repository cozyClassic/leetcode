/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function(words) {
    let mors = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    let alphas = "abcdefghijklmnopqrstuvwxyz"
    let hashs = {}
    for (let i=0; i<26; i++) {
        hashs[alphas[i]] = mors[i]
    }
    results = new Set()
    
    for (const word of words) {
        let result = ""
        for (const w of word) {
            result += hashs[w]
        }
        results.add(result)
    }
    return results.size
};