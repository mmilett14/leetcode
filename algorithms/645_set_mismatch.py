# https://leetcode.com/problems/set-mismatch/

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        corrected_nums = []
        
        for i in range(0, len(nums)-1):
            
            if nums[i] == nums[i+1]:
                
                corrected_nums.append(nums[i])
                corrected_nums.append(nums[i]+1)
                
        return corrected_nums
