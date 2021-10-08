-- https://leetcode.com/problems/minimum-index-sum-of-two-lists/submissions/

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        smallest_diff = float('inf')
        favorite = []
        
        for i in range(0, len(list1)):
            
            for j in range(0, len(list2)):
                
                if list1[i] == list2[j]:
                    
                    if (i + j) < smallest_diff:
                        favorite = [list1[i]]
                        smallest_diff = i + j
                    
                    elif (i + j) == smallest_diff:
                        favorite.append(list1[i])
        
        return favorite
