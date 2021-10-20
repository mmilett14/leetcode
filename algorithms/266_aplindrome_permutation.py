# https://leetcode.com/problems/palindrome-permutation/

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        char_counter = {}
        odd_counter = 0
        
        for char in s:
            
            if char not in char_counter:
                char_counter[char] = 1
            
            else:
                char_counter[char] += 1
                
        for char in char_counter:
            
            if char_counter[char] % 2 == 1:
                odd_counter += 1
        
        if odd_counter > 1:
            return False
        
        else:
            return True
