# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        lastNonZeroFoundAt = 0
        
        for num in nums:
            if num != 0:
                nums[lastNonZeroFoundAt] = num
                lastNonZeroFoundAt += 1
        
        for i in range(lastNonZeroFoundAt, len(nums)):
            nums[i] = 0
