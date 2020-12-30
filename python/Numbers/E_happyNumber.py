class Solution:
    def isHappy(self, n: int) -> bool:
        
        def checkIfHappy(number):
            sum = 0

            while number > 0:
                number,y = divmod(number,10)
                sum += y**2

            return sum

        if n == 1:
            return True
        
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = checkIfHappy(n)
            
        return n == 1
        
    
print(Solution().isHappy(19))