# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        int_list = []        
        
        roman_as_int = 0

        for i in range(0, len(s)):
            
            int_list.append(roman_dict[s[i]])
        
        for i in range(0, len(int_list)-1):
            
            if (int_list[i] > int_list[i+1]) | (int_list[i] == int_list[i+1]):
                roman_as_int += int_list[i]
            
            elif int_list[i] < int_list[i+1]:
                roman_as_int -= int_list[i]
        
        roman_as_int += int_list[len(int_list)-1]
        
        return roman_as_int
