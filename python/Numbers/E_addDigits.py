class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            x,y = divmod(num,10)
            num = x + y
            
        return num

print(Solution().addDigits(99471))