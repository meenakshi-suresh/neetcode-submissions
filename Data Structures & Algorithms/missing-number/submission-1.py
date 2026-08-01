class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans,a = 0,0
        for i in range(len(nums)+1):
            ans = ans ^ i
        for i in range(len(nums)):
            a = a ^ nums[i]
        return ans ^ a