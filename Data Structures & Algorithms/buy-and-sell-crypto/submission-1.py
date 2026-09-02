class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for i in prices:
            if i < buy:
                buy = i
            current_profit = i - buy
            if current_profit > profit:
                profit = current_profit


        return profit
        