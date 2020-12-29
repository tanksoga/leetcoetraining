class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        seen = {}
        
        for index,value in enumerate(numbers):
            remain = target - value
            
            if remain in seen:
                return [seen[remain] + 1,index + 1]
            else:
                seen[value] = index
                
        return []
                
                
nums = [2,7,11,15] 
target = 9 

print(Solution().twoSum(nums,target))