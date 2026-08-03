class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0
        answer = float("inf")
        left = 0
        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                answer = min(answer,right-left+1)
                window_sum -= nums[left]
                left+=1
        return 0 if answer == float("inf") else answer