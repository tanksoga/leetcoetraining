class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        exist1 = {}
        exist2 = {}
        pattern1 = []
        pattern2 = []
        
        for i in range(len(s)):
            if(s[i] not in exist1):
                exist1[s[i]] = str(i)
                pattern1.append(str(i))
            else:
                pattern1.append(exist1[s[i]])
        
        for i in range(len(s)):
            if(t[i] not in exist2):
                exist2[t[i]] = str(i)
                pattern2.append(str(i))
            else:
                pattern2.append(exist2[t[i]])
        
        return pattern1 == pattern2
                
                
print(Solution().isIsomorphic("title","paper"))

print(Solution().isIsomorphic("title","apple"))