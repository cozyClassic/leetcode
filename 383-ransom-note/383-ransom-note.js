/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    while (ransomNote.length > 0) {
        let char = ransomNote.charAt(0)
        let old_m_length = magazine.length
        magazine = magazine.replace(char,"")

        if (old_m_length == magazine.length){
            return false
        }
        ransomNote = ransomNote.substring(1)
    }
    
    return true
};