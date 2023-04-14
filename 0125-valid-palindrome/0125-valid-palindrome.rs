impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let mut iter = s.chars()
            .filter(|c: &char| c.is_alphanumeric())
            .map(|c: char| c.to_lowercase());

    while let (Some(c1), Some(c2)) = (iter.next(), iter.next_back()) {
        if !c1.eq(c2)  {
            return false;
        }
    }
    return true;
    }
}