class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        maxLen = max(len(a), len(b))
        a, b = a.zfill(maxLen), b.zfill(maxLen)
        
        carry = 0
        result = []
        
        for index in range(maxLen - 1, -1, -1):
            if a[index] == "1":
                carry += 1
            if b[index] == "1":
                carry += 1
                
            if carry % 2 == 1:
                result.append("1")
            else:
                result.append("0")
                
            carry = carry // 2

        if(carry == 1):
            result.append("1")
        
        result.reverse()
        
        return "".join(result)
        
print(Solution().addBinary("11101","1100"))