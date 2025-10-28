class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # A = sorted(s)
        # B = sorted(t)

        # return A == B

        mapA = {}
        mapB = {}

        for ch in s:
            mapA[ch] = mapA.get(ch, 0)+1
        
        for ch in t:
            mapB[ch] = mapB.get(ch,0) +1


        

        
        
        print(mapA)

        return mapA == mapB
        