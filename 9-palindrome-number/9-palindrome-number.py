class Solution:
    def isPalindrome(self, x: int) -> bool:
        origin = str(x)
        return origin == origin[::-1]