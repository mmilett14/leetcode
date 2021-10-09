# https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        current_subarray = 0
        max_subarray = -float('inf')
        
        for i in range(0, len(nums)):
            
            current_subarray += nums[i]
            
            if current_subarray > max_subarray:
                max_subarray = current_subarray
            
            if current_subarray < 0:
                current_subarray = 0
                
        return max_subarray
