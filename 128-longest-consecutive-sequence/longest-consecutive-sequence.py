class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen = set(nums)
        ans = 0

        for num in seen:

            if (num - 1 ) not in seen:

                c = 0
                curr = num

                while curr in seen:
                    c +=1
                    curr +=1
                
                ans = max(ans, c)
        return ans

        