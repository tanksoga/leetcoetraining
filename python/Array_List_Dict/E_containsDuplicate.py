from collections import Counter
class Solution:
    def containsDuplicate(self, nums) -> bool:
        
        count = Counter(nums)
        
        for i in count.keys():
            if count[i] > 1:
                return True
        
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))