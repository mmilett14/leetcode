class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        new_num = []
        
        for num in range(k, len(nums), 1):
            new_num.append(nums[num])

        for num in range(0, k, 1):
            new_num.append(nums[num])
        
        return new_num
