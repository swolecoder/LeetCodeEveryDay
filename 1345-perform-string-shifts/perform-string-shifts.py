class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        if not s:
            return 

        
        net = 0

        for dir, amt in shift:
            if dir == 0:
                net -= amt
            else:
                net += amt
            
        
        net %= len(s)

        print(net)

        if net == 0:
            return s
        
        return s[-net:] + s[:-net]