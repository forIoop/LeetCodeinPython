#Given a list of prices where i is a price of a given stock at that day,
#find the maximum profit that you can get from the list of prices.

prices  = [2,4,6,2,7,2,9,4,0,19,34,31,24,23]

class Solution:
    def maxProfit(prices) -> int:

        max_profit = 0

        for i in range(0,len(prices)):
            for j in range(i+1, len(prices)):
                min_price = prices[j] - prices[i]
                if min_price> max_profit:
                    max_profit = min_price
        return max_profit

    print(maxProfit(prices))
