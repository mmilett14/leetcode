# https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        x_str = str(x)
        
        x_rev = str(x)[::-1]
        
        if x_str == x_rev:
            return True
        
        else:
            return False
