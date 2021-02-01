class Solution(object):
    def maxCrossingSum(self,arr, l, m, h):
        
        # Include elements on left of mid.
        sm = 0
        left_sum = -10000
    
        for i in range(m, l-1, -1):
            sm = sm + arr[i]
    
            if (sm > left_sum):
                left_sum = sm
    
        # Include elements on right of mid
        sm = 0
        right_sum = -1000
        for i in range(m + 1, h + 1):
            sm = sm + arr[i]
    
            if (sm > right_sum):
                right_sum = sm
    
        print("======> maxCrossingSum : " + str(left_sum + right_sum) + "," + str(left_sum) + "," + str(right_sum))

        # Return sum of elements on left and right of mid
        # returning only left_sum + right_sum will fail for [-2, 1]
        return max(left_sum + right_sum, left_sum, right_sum)
    
    
    # Returns sum of maxium sum subarray in aa[l..h]
    def maxSubArraySum(self, arr, l, h):
    
        # Base Case: Only one element
        if (l == h):
            print (" Return arr[1]:" + str(arr[l]))
            return arr[l]
    
        # Find middle point
        m = (l + h) // 2

        print("maxSubArraySum : " + str(l) + "," + str(m) + "," + str(h))
    
        # Return maximum of following three possible cases
        # a) Maximum subarray sum in left half
        # b) Maximum subarray sum in right half
        # c) Maximum subarray sum such that the
        #     subarray crosses the midpoint
        return max(self.maxSubArraySum(arr, l, m),
                self.maxSubArraySum(arr, m+1, h),
                self.maxCrossingSum(arr, l, m, h))

arr = [2, 3, 4, 5, 7]
n = len(arr)
 
max_sum = Solution().maxSubArraySum(arr, 0, n-1)
print("Maximum contiguous sum is ", max_sum)