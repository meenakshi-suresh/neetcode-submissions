class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        l = len(self.nums)
        prefix = [0] * (l+1)
        for i in range(1,l+1):
            prefix[i] = prefix[i-1] + self.nums[i-1]
        return prefix[right + 1] - prefix[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)