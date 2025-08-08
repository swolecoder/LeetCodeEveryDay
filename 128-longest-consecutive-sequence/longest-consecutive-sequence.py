class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ans = 0
        if not nums:
            return 0

        for num in seen:
            if num -1 not in seen:
                curr = num 
                count = 0

                while curr in seen:
                    curr +=1
                    count +=1
                ans = max(count, ans)
        return ans
                
        