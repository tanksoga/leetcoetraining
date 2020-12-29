class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        #s = "a example     text"
        
        #print(s.split())
        #print(list(reversed(s.split())))
        #print(" ".join(reversed(s.split())))
        
        return " ".join(reversed(s.split()))
        

print(Solution().reverseWords("Your reversed string should not contain leading or trailing spaces."))