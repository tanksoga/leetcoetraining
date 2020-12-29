class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        charMap = {")":"(",
                  "]":"[",
                  "}":"{"}
        
        stack = []
        
        for char in s:
            if char in charMap.keys():
                if not stack:
                    return False
                element = stack.pop()   
                if(element != charMap[str(char)]):
                    return False
            else:
                stack.append(char)
                
        return not stack
        
        
        
            
        
print(Solution().isValid("{()[()]}"))