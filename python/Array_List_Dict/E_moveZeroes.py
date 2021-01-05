class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) == 0:
            return None
        
        length = len(nums)
        
        lastNonZero = 0;
        
        i = 0
        
        for i in range(length):
            if(nums[i] != 0):
                nums[lastNonZero] = nums[i]
                lastNonZero += 1
            
        while lastNonZero < length:
            nums[lastNonZero] = 0
            lastNonZero += 1
            
        return nums

print(Solution().moveZeroes([0,3,4,6,11,0,23,1,3,5,0]))