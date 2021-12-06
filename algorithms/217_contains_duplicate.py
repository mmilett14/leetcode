# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        counter = {}
        
        nums.sort()
        
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                return True
        
        return False
