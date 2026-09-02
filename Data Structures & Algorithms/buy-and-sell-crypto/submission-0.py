class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for i in prices:
            if i < buy:
                buy = i
            current_price = i - buy
            if current_price > profit:
                profit = current_price


        return profit
        