class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # given array of prices
        # each item is the price on ith day
        # choosing a single to buy
        # choosing a diff day in future to sell
        # return max progit you can recieve

        left, right = 0, 1
        tempProfit = 0

        maxProfit = 0

        while right < len(prices):
            tempProfit = prices[right] - prices[left]
            maxProfit = max(maxProfit, tempProfit)

            if prices[right] < prices[left]:
                left = right

            # we wanna go until 
            right += 1

        return 0 if maxProfit < 0 else maxProfit