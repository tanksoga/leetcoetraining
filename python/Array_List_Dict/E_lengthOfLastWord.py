class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        adjustString = s.strip()
        length = len(adjustString)
        
        for index in reversed(range(length)):
            if(adjustString[index] == " "):
                return length - index - 1
            
        return length
        
print(Solution().lengthOfLastWord("My name is Henry Chen"))