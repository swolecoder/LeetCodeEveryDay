class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        for w in words:
            l = 0 
            r = len(w) -1

            while w[l] == w[r]:
                if l >= r:
                    return w
                
                l +=1
                r -=1
        return ""
            # if w == w[::-1]:
            #     return w
        return ""
        