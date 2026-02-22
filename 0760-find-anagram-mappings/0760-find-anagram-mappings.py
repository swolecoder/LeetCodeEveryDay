class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        m = defaultdict(int)

        for i in range(len(nums2)):
            m[nums2[i]] = i

        

        ans = [0] * len(nums1)

        for i in range(len(nums1)):
            ans[i] = m[nums1[i]]


        return ans        