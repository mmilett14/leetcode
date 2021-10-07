# https://leetcode.com/problems/keyboard-row/

class Solution(object):
    def to_upper(self, alphalist):
        
        for i in range(0, len(alphalist)):
            
            alphalist.append(alphalist[i].upper())
            
        return alphalist
    
    
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        row_first = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        row_first = Solution.to_upper(self, row_first)
        row_second = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        row_second = Solution.to_upper(self, row_second)
        row_third = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        row_third = Solution.to_upper(self, row_third)
        
        single_row_words = []
        
        for word in words:
            
            row_first_count = 0
            row_second_count = 0
            row_third_count = 0
            
            for i in range(0, len(word)):
                
                if word[i] in row_first:
                    row_first_count += 1
                
                elif word[i] in row_second:
                    row_second_count += 1
                    
                elif word[i] in row_third:
                    row_third_count += 1
                
            if (len(word) == row_first_count) | (len(word) == row_second_count) | (len(word) == row_third_count):
                single_row_words.append(word)
        
        return single_row_words
                    
