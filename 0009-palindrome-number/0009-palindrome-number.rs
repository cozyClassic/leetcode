impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 { 
            return false
        }
        let mut _x = x;
        let mut y = 0;
        while _x > 0 {
            y = y * 10 + _x % 10;
            _x /= 10;
        }
        x == y
    }
}