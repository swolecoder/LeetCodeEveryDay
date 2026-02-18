class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1] * len(arr)
        fMax = -1

        for i in range(len(arr)-1,-1,-1):
            ans[i] = fMax
            fMax = max(fMax,arr[i])

        return ans