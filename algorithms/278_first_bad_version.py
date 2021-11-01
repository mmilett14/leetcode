# https://leetcode.com/problems/first-bad-version/
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        left = 0
        right = n
        mid = (left + right) // 2
        
        bad_version = float('inf')
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if isBadVersion(mid) == True:
                
                if isBadVersion(mid-1) == False:
                    bad_version = mid
                    return bad_version
                
                else:
                    right = mid + 1
            
            else:
                left = mid+1
        
        return bad_version
