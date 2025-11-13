class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        foundMin = prices[0]


        for p in prices:

            ans = max(ans, p- foundMin )

            foundMin = min(foundMin, p)
        return ans

        