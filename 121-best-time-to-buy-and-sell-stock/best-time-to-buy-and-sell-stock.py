class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        high = 0
    

        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            else:
                high = max(high, prices[i] - lowest)
        return high