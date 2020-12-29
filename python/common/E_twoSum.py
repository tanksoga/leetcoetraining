class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        numsLength = len(nums)
        
        if(numsLength < 2):
            return list()
        
        for x in range(numsLength) :
            if(x <= (numsLength - 2)):
                y = x + 1
                for y in range(numsLength):
                    if(nums[x] + nums[y] == target):
                        result = []
                        result.append(x)
                        result.append(y)
                        return result
        '''            
        seen = {}
        for index, value in enumerate(nums):
            remain = target - value
            if remain in seen :
                return [index,seen[remain]]
            else:
                seen[value] = index
        return []   

nums = [2,7,11,15] 
target = 9 

print(Solution().twoSum(nums,target))