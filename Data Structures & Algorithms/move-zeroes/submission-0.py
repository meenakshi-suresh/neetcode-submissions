class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        scan = 0
        write = 0
        while scan < len(nums):
            if nums[scan] != 0:
                nums[write],nums[scan] = nums[scan],nums[write]
                write += 1
            scan += 1