from collections import defaultdict

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        itemMap = defaultdict(int)
        for i in nums:
            itemMap[i] += 1
                
        for i in itemMap:
            if itemMap[i] == 1:
                return i

print(Solution().singleNumber([4,1,2,1,2]))