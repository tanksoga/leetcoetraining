class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        minDis = len(words)
        
        if(minDis < 2):
            return 0
        
        w1Index = -1
        w2Index = -1
        
        for index in range(len(words)):
            if(words[index] == word1):
                w1Index = index
            elif(words[index] == word2):
                w2Index = index
                
            if(w1Index != -1 and w2Index != -1):
                currentDis = w2Index - w1Index
                if(currentDis < 0):
                    currentDis *= -1

                if currentDis < minDis:
                    minDis = currentDis
                
        return minDis

print(Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"],"practice","coding"))