from collections import Counter

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = Counter(bin(n)[2:])

        return count['1']
        
print(Solution().hammingWeight(301))