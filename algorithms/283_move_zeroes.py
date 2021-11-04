class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nums_no_zeros = nums.copy()
        nums_no_zeros[:] = [num for num in nums if num != 0]

        zero_cnt = len(nums) - len(nums_no_zeros)

        nums = nums_no_zeros.copy()

        for zero in range(zero_cnt):
            nums.append(0)
