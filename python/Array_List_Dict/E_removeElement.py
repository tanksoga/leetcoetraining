class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        i = 0
        while i < len(nums):
            if(nums[i] == val):
                del nums[i]
            else:
                i += 1

        print(nums)     
        return len(nums)
        
print(Solution().removeElement([1,1,3,4,5,5,6,7,7,7],7))