# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        parens = {'(': ')', '[': ']', '{': '}'}
        parens_rev = {')': '(', ']': '[', '}': '{'}
        
        stack = []
        
        for char in s:
            if char in parens:
                stack.append(char)
            else:
                if parens_rev[char] == stack[len(stack)-1]:
                    stack.pop()
                else:
                    return False
            
        if len(stack) == 0:
            return True
        else:
            return False
