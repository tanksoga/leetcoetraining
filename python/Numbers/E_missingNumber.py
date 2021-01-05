class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numSet = set(nums)
        
        i = 0
        
        while i <= len(nums):
            if i not in numSet:
                return i 
            i += 1
            
        
print(Solution().missingNumber([0,1,3,4]))