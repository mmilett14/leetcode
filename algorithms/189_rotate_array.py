class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for num in range(k):
            pop = nums.pop(len(nums)-1)
            nums.insert(0, pop)
