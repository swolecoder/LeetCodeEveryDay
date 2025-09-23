class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:


        def helper(i, xor):

            if i == len(nums):
                return xor
            
            include = helper(i +1, nums[i] ^ xor)
            exclude = helper(i +1, xor)

            return include + exclude
        

        return helper(0,0)
        