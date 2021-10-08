# https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sum_biggest = -float('inf')

        size_window = 1

        while size_window <= len(nums):

            for i in range(0, len(nums)):

                sum_window = sum(nums[i:i+size_window])

                if sum_window > sum_biggest:
                    sum_biggest = sum_window

            size_window += 1
            
        return sum_biggest
