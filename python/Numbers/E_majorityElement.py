from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = Counter(nums)
        n = len(nums) / 2
        
        for value in count:
            time = count[value]
            if(time > n):
                return value
            
        
print(Solution().majorityElement([2,2,1,1,1,2,2,4,6,2,2,2,2,2]))