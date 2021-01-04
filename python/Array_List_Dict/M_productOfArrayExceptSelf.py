class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        
        left = [0]*length
        right = [0]*length
        result = [0]*length
        
        if(length == 1):
            return [0]
        
        left[0] = 1
        right[length - 1] = 1
        
        for i in range(1, length):
            left[i] = left[i - 1] * nums[i - 1]
            
        right[length - 1] = 1
        
        for i in reversed(range(length - 1)):
            right[i] = right[i + 1] * nums[i + 1]
            
        for i in range(length):
            result[i] = left[i] * right[i]
            
        return result
                
        
print(Solution().productExceptSelf([1,3,5,7,8,10,4]))