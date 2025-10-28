class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # seen = set()

        # for n in nums:
        #     if n in seen:
        #         return True
        #     seen.add(n)
        
        # return False

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        
        return False


        