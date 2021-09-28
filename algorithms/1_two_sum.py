# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        start = 0
        end = len(nums)-1
        
        while start < end:
            
            for i in range(start, end):
                
                if nums[start] + nums[i+1] == target:
                    return start, i+1
            
            start += 1
            
        return -1
