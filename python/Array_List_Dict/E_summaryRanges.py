class Solution:
    def summaryRanges(self, nums):
        
        result = []
        
        start = -1
        end = -1
        i = 0
        n = 1
        
        total = len(nums)
        
        while i < total:
            start = i
            while i + n <= total:
                if i + n < total:
                    if nums[i + n] - nums[i + n - 1] == 1:
                        n += 1
                    else:
                        end = i + n - 1
                        if start != end:
                            result.append(str(nums[start]) + "->" + str(nums[end]))
                        else:
                            result.append(str(nums[start]))
                        print(result)
                        break
                else:
                    start = i
                    end = i + n -1
                    if start == end:
                        result.append(str(nums[start]))
                    else:
                        result.append(str(nums[start]) + "->" + str(nums[end]))
                    i = end + 1
                
            i = end + 1
            n = 1
            
        return result

print(Solution().summaryRanges([0,2,3,4,6,8,9]))