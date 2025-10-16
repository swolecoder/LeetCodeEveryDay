class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        c , e = 0,0

        for ch in s:

            if ch == "(":
                c+=1
            else:
                if c > 0:
                    c -=1
                else:
                    e +=1
        return c + e

        