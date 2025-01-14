class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = prices[0]
        for i in range(len(prices)):
            ans = max(ans, prices[i] - buy)
            buy = min(buy, prices[i])
        return ans
        