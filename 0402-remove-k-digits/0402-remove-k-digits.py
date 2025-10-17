class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for n in num:

            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -=1
            
            stack.append(n)
        
        while k > 0:
            k -=1
            stack.pop()

        ans = ''.join(stack).lstrip("0")

        

        return  "0" if not ans else ans

        