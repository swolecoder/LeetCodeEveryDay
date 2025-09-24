class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        foundMax = -1
        ans = [-1] * len(arr)

        for i in range(len(arr)-1,-1,-1):
            ans[i] = foundMax
            foundMax = max(foundMax,arr[i])
        return ans
