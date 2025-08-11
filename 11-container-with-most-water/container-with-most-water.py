class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) -1
        ans = 0
        print(j)

        while i < j:

            h = min(height[i], height[j]) * (j-i)
            print(h, i, j)
            ans = max(ans, h)
            if height[i] > height[j]:
                j -=1
            else:
                i +=1
        return ans

                    