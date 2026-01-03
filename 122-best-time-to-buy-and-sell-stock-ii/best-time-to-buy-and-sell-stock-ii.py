class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initializing pointers
        left, right = 0, 1
        profits = 0

        # go increment through loop and find profits
        while right < len(prices):
                if prices[right] > prices[left]:
                    profits += prices[right] - prices[left]
      
                left += 1
                right += 1
                
        
        return profits