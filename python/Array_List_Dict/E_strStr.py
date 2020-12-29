class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        l1 = len(needle)
        targetL = len(haystack)
        
        for index in range(targetL - l1 + 1):
            if haystack[index:index + l1] == needle:
                return index
            
        return -1
        
print(Solution().strStr("hello","ll"))