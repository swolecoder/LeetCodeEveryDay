class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        print(s)

        def reverse(i,j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i +=1
                j -=1
            


        i = 0
        while i < len(s):
            if s[i] != " ":
                j = i

                while j < len(s) and s[j] != " ":
                    j +=1
                
                # reversed
                reverse(i, j-1)

                i = j +1

        return ''.join(s)
        