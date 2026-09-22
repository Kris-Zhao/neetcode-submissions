class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # L=buy, R=sell
        L = 0
        maxP = 0
        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            else:
                maxP = max(maxP, prices[R] - prices[L])
        return maxP