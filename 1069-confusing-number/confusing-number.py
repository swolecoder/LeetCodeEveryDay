class Solution:
    def confusingNumber(self, n: int) -> bool:

        map = {
            "0":"0",
            "1":"1",
            "6":"9",
            "8":"8",
            "9":"6"
        }



        ans = ""

        for ch in str(n):
            print(ch)
            if ch not in map:
                return False
            
            ans = map[ch] + ans
        

        print(ans)
        return ans != str(n)
        