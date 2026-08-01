class Solution:
    def mySqrt(self, x: int) -> int:
        low, high, ans = 0,x,0
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
                ans = mid
        return ans