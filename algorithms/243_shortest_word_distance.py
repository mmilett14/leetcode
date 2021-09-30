# https://leetcode.com/problems/shortest-word-distance/

class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        word1_spot = 0
        word2_spot = 0
        
        for i in range(0, len(wordsDict)):
            
            if wordsDict[i] == word1:
                word1_spot = i
            
            elif wordsDict[i] == word2:
                word2_spot = i
                     
            distance = abs(word1_spot - word2_spot)
            
            if distance == 1:
        
                return distance
        
        return distance
        
