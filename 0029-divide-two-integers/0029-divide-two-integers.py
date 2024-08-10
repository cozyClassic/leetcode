class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_minus = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1

        dividend, divisor = abs(dividend), abs(divisor)

        count = 0

        while dividend >= divisor:
            curr, mul = divisor, 1
            while dividend >= curr:
                dividend -= curr
                count += mul
                curr += curr
                mul += mul
        count = min(count, pow(2,31)-1)
        return count if is_minus == 1 else -count