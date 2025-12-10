class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0,1
        maxprofit = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
                right += 1
            else:
                profit = prices[right]-prices[left] 
                maxprofit = max(profit,maxprofit)
                right += 1
        return maxprofit

