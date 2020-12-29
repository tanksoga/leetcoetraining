class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 0:
            return None
        if numRows == 1:
            return [[1]]
        
        result = [[1]]
        
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(result[i - 1][j - 1] + result[i - 1][j])
            row.append(1)
            result.append(row)
            
        return result
        
print(Solution().generate(10))