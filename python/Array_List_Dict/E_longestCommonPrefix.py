class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        result = list()
        
        for string in zip(*strs):
            if(len(set(string)) == 1):
                result.append(str(string[0]))
            else:
                break
                
        return "".join(result)

        
strs = ["flower","flow","flight"]

print(Solution().longestCommonPrefix(strs))