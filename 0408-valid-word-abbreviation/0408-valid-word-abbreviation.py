class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0 
        j = 0
        n = len(word)
        m = len(abbr)

        while i < n and j < m:

            if abbr[j] == '0':
                return False
            
            if word[i] == abbr[j]:
                i  +=1
                j +=1
            elif abbr[j].isalpha():
                return False
            else:
                c = 0
                while j < m and abbr[j].isdigit():
                    c = c* 10 + int(abbr[j])
                    j +=1
                
                i += c
            

        return i == n and j == m