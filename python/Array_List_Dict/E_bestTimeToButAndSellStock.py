class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if prices == []:
            return 0
        
        min = 100000000
        profit = 0
        
        for day in range(len(prices)):
            if prices[day] < min:
                min = prices[day]
            else:
                if prices[day] - min > profit:
                    profit = prices[day] - min
                    
        return profit
        
print(Solution().maxProfit([7,1,5,3,6,4]))