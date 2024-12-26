class Solution(object):
    def maxProfit(self, prices):
        # [7,1,5,3,6,4]
        #    i r
       
        i = 0
        max_profit = 0
        for r in range(1, len(prices)):
            if prices[r] > prices[i]:
                profit = prices[r] - prices[i]
                max_profit = max(profit, max_profit)
            else:
                i = r

        return max_profit    




        """
        :type prices: List[int]
        :rtype: int
        """
        