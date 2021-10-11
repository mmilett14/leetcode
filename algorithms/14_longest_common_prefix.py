class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        current_prefix = ""
        final_prefix = ""
        prefix_counter = 1
        
        for i in range(0, len(strs[0])):
            
            current_prefix = strs[0][i:i+1]
            
            for j in range(1, len(strs)):
                
                if strs[j][i:i+1] == current_prefix:
                    prefix_counter += 1
            
            if prefix_counter == len(strs):
                final_prefix += current_prefix
                prefix_counter = 1
            
            else:
                return final_prefix
            
        return final_prefix
