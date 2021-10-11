class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        final_prefix = ""
        current_prefix = ""
        
        k = 0
        j = 1
        
        for i in range(0, len(strs)):
            
            current_prefix = strs[0][k:k+1]
            
            while j <= len(strs)-1:
                
                if strs[j][k:k+1] == current_prefix:
                    j += 1
            
            if j == len(strs):
                final_prefix += current_prefix 
                k += 1
                j = 1
            
            else:
                return final_prefix
        
        return final_prefix
