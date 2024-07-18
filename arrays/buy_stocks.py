# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

#O(n^2): inefficient
def maxProfit(prices):
        max_profit = 0
        for i in range(len(prices)):
            buy_price = prices[i]
            for j in range(len(prices)):
                if i < j:
                    profit = prices[j] - buy_price
                    if profit > max_profit:
                        max_profit = profit
        return max_profit

# def maxProfit2(prices):
#      min = float('inf')
#      max_profit = 