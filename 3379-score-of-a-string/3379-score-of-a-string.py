class Solution:
    def scoreOfString(self, s: str) -> int:
        print(ord("h"))

        sum = 0
        prev = ord(s[0])

        for i in range(1,len(s)):
            sum += abs(prev - ord(s[i]))
            prev = ord(s[i])



        return sum 
        