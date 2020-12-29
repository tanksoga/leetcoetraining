from collections import defaultdict

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        itemMap = defaultdict(int)
        for i in nums:
            itemMap[i] += 1
                
        for i in itemMap:
            if itemMap[i] == 1:
                return i

print(Solution().singleNumber([0,1,0,1,0,1,99]))