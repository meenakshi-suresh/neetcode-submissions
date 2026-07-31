class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = []
        prefix = [1] * length
        suffix = [1] * length
        for i in range(1,length):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(length-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(length):
            output.append(prefix[i] * suffix[i])
        return output
