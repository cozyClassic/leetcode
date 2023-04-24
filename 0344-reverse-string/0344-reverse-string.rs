impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        let L = s.len();
        for index in 0..L/2 {
            s.swap(index, L-1-index)
        }
    }
}