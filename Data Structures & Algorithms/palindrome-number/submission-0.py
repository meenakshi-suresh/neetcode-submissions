class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10
        return rev == original
        