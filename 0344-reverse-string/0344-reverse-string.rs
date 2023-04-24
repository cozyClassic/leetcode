impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        let L = s.len();
        for index in 0..L/2 {
            let temp:char = s[index];
            s[index] = s[L-1-index];
            s[L-1-index] = temp;
        }
    }
}