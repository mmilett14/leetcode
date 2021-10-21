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
                if len(stack) == 0:
                    return False
                elif parens_rev[char] != stack[len(stack)-1]:
                    return False
                else:
                    stack.pop()
            
        if len(stack) == 0:
            return True
        else:
            return False
