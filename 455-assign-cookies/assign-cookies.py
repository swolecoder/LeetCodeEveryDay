class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        i =0
        count =0

        for j in range(len(s)):
            if i < len(g) and g[i] <= s[j]:
                count +=1
                i +=1
        return count 

        