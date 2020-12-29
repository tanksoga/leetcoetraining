class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        romanMap = {"I":1,
                   "V":5,
                   "X":10,
                   "L":50,
                   "C":100,
                   "D":500,
                   "M":1000}
        result = 0
        index = 0
        
        while index < len(s):            
            if index + 1 < len(s) and (romanMap[s[index]] < romanMap[s[index + 1]]):
                result = result + (romanMap[s[index + 1]] - romanMap[s[index]])
                index += 2
            else:
                result = result + romanMap[s[index]]
                index += 1
                    
        return result

print(Solution().romanToInt("IVIXC"))                