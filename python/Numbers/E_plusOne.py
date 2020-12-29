class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        length = len(digits)
        
        carry = 0
        result = []
        for index in range(length - 1, -1, -1):
            
            if(index == length - 1):
                sumOfThisDigit = digits[index] + 1 + carry
            else:
                sumOfThisDigit = digits[index] + carry
            
            if(sumOfThisDigit > 9):
                result.append(sumOfThisDigit % 10)
                carry = sumOfThisDigit // 10
            else:
                result.append(sumOfThisDigit)
                carry = 0
                
        if(carry > 0):
            result.append(carry)
            
        result.reverse()
        
        return result
                
print(Solution().plusOne([3,7,9,9,9]))