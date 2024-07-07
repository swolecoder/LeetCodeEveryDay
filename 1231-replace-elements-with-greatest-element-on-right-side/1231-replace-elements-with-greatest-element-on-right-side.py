class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ele = -1
        ans = [0] * len(arr)

        for i in range(len(arr)-1,-1,-1):
            ans[i] = ele
            ele = max(ele, arr[i])
        return ans 
        