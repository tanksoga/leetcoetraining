class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        patternList = list(pattern)
        wordList = s.split()
        
        if(len(patternList) != len(wordList)):
            return False
        
        patternMap = {}
        
        for i in range(len(patternList)):
            if patternList[i] not in patternMap:
                if wordList[i] not in patternMap.values():
                    patternMap[str(patternList[i])] = str(wordList[i])
                else:
                    return False
            else:
                if patternMap[str(patternList[i])] != str(wordList[i]):
                    return False
                
        return True
            
print(Solution().wordPattern("abcbad","dog cat pig cat dog dock"))
print(Solution().wordPattern("abcbad","dog cat pig cat dog dog"))