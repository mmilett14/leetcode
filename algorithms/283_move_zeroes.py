class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nums_no_zeros = nums
        nums_no_zeros.remove(0)
        
        zero_cnt = len(nums) - len(nums_no_zeros)
        
        nums.remove(0)
        
        # 0s are not being appended to end of nums. Issue with zero_cnt... not sure what, though.
        
        for zero in range(zero_cnt):
            nums.append(0)
