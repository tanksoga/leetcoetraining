class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            center = (left + right) // 2
            
            if(nums[center] == target):
                return center
            elif(nums[center] < target):
                left = center + 1
            else:
                right = center - 1
                
        return left
                
print(Solution().searchInsert([1,2,4,5,7,9,10],4))