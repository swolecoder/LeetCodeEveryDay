class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = prices[0]

        for p in prices:
            ans = max(ans,p-buy,0 )
            buy = min(buy,p)
        return ans        