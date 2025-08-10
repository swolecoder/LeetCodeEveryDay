from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        if n < 3:
            return []

        ans: List[List[int]] = []

        for i in range(n - 2):
            # Skip duplicate anchors (do NOT mutate i; just continue)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    ans.append([nums[i], nums[j], nums[k]])  # list, not tuple
                    j += 1
                    k -= 1
                    # Skip duplicates on the left after moving j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # Skip duplicates on the right after moving k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif total < 0:
                    j += 1          # sum too small → move left pointer right
                else:
                    k -= 1          # sum too large → move right pointer left

        return ans
