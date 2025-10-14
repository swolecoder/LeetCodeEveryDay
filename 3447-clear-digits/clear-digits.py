class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch in "abcdefghijklmnopqrstuvwxyz":
                stack.append(ch)
            else:
                stack.pop()
        
        return "".join(stack)
        