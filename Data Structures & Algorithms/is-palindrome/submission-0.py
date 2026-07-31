class Solution:
    def isPalindrome(self, s: str) -> bool:
        copy = ''.join([c.lower() for c in s if c.isalnum()])
        left = 0
        right = len(copy) - 1
        while left < right:
            if copy[left] != copy[right]:
                return False
            left += 1
            right -= 1
        return True

