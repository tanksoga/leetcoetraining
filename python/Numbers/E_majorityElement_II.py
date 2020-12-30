from collections import Counter

class Solution:
    def majorityElement(self, nums):
        
        count = Counter(nums)
        target = len(nums) / 3
        
        result = []
        
        for i in count.keys():
            if(count[i] > target):
                result.append(i)
        
        return result

print(Solution().majorityElement([2,2,1,1,1,2,2,4,6,2,2,2,2,2]))        