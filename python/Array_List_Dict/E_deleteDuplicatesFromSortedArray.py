class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0

        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i]
            else:
                i += 1
                
        print(nums)        
        return len(nums)
                
        
        
print(Solution().removeDuplicates([1,1,3,4,5,5,6,7,7,7]))