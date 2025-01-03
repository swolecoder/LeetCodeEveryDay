class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = defaultdict(int)
        if len(s) != len(t):
            return False

        for ch in s:
            dict[ch] +=1
        
        print(dict)

        for ch in t:
            if ch not in dict:
                return False
            dict[ch] -=1
            if dict[ch] == 0:
                del dict[ch]
        return True

        # return ''.join(sorted(s)) == ''.join(sorted(t))
        