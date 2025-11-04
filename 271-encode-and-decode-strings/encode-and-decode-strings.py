class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans = ""

        for ch in strs:
            ans += str(len(ch))+"#"+ ch
        
        print(ans)
        return ans

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        ans = []
        i = 0

        while i < len(s):
            j = i 

            while j < len(s) and s[j] != "#":
                j +=1
            
            lenF = int(s[i:j])
            print(int(lenF))
            data = s[j+1: j+ lenF+1]
            print(data)

            i = j+1 +lenF
            ans.append(data)

            
        
        return ans
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))