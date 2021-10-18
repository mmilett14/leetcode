# https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        triangle = []
        
        for row_num in range(numRows):
            
            row = [None for _ in range(0, row_num+1)]
            row[0], row[-1] = 1, 1
            
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j-1] + triangle[row_num - 1][j]
            
            triangle.append(row)
            
        return triangle
