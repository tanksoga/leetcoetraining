from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        sDict = Counter(s)
        tDict = Counter(t)
        
        return sDict == tDict
        
print(Solution().isAnagram("anagram","nagaram"))