class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans = ""
        for data in strs:
            ans += str(len(data)) + "#" + data
        return ans
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        i = 0
        ans = []
        print(s)
        while i < len(s):
            j = i
            while  s[i] != "#" and i < len(s):
                i +=1
            foundL = s[j:i]
            foundS = s[i+1: i+1 + int(foundL)]
            ans.append(foundS)
            i += int(foundL) + 1
        return ans
        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))