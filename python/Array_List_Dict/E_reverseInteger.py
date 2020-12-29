class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x <= -2**31 or x >= 2**31-1:
            return 0
        
        xString = str(x)
        if(x < 0):
            xString = xString[1:]
            reserved = "-" + xString[::-1]
        else:
            reserved = xString[::-1]
        
        result = int(reserved)
        
        if result <= -2**31 or result >= 2**31-1:
            return 0
        else:
            return result

print(Solution().reverse(3560745))