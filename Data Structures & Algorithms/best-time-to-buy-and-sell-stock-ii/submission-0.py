#My idea is to scan the prices while looking one day ahead. If tomorrow's price is higher than today's, I buy (or continue holding if I already own the stock). As long as each following day's price continues to increase, I keep holding because selling early would miss additional profit. When I find that the next day's price is lower than the current day's price, I sell on the current day since it is the local peak. After that, I continue scanning for the next increasing sequence and repeat the same process. In other words, I treat each continuous upward trend as a single buy-and-hold transaction, selling only when the trend ends before starting the next transaction.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        stock_owned = 0
        price = 0
        for i in range(len(prices)):
            if (i + 1) < len(prices):
                if stock_owned == 0:
                    if prices[i + 1] > prices[i]:
                        stock_owned = 1
                        price = prices[i]
                if stock_owned == 1:
                    if prices[i + 1] < prices[i]:
                        stock_owned = 0
                        profit += prices[i] - price
        if stock_owned == 1:
            profit += prices[i] - price
        return profit 
        