class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        openToClose = {
            "(":")",
            "[":"]",
            "{":"}"
        }

        for ch in s:
            if ch in openToClose:
                stack.append(ch)
            else:

                if not stack:
                    return False
                
                lastSeen = stack.pop()

                if openToClose[lastSeen] != ch:
                    return False
        return len(stack) == 0
        