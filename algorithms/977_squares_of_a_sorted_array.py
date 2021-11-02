# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        squares = []
        
        for num in nums:
            square = abs(num*num)
            squares.append(square)
        
        squares.sort()
        
        return squares
