class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyprice = -1
        profit = 0
        for i in range(len(prices)):
            if i == 0:
                buyprice = prices[i]
                continue
            if prices[i] < buyprice:
                buyprice = prices[i]
                continue
            if prices[i] - buyprice > profit:
                profit = prices[i] - buyprice
        return profit
            
