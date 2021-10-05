# https://leetcode.com/problems/shortest-word-distance/

class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        limit = (3 * 10**4)+1
        
        found1 = limit
        found2 = limit
        distance = limit
        
        
        for i in range(0, len(wordsDict)):
            
            if wordsDict[i] == word1:
                found1 = i
                
                if abs(found1 - found2) < distance:
                    distance = abs(found1 - found2)
            
            elif wordsDict[i] == word2:
                found2 = i
                
                if abs(found1 - found2) < distance:
                    distance = abs(found1 - found2)
                    
        return distance
