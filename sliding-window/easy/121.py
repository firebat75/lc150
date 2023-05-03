class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, output = 0, 1, 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                output = max(output, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1

        return output
