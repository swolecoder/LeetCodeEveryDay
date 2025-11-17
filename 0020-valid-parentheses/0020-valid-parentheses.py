class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]

        map = {
            "(":")",
            "[":"]",
            "{":"}"
        }


        for o in s:

            if o in map:
                stack.append(o)
            else:

                if not stack:
                    return False
                
                lastData = stack.pop()
                if map[lastData] != o:
                    return False
        return len(stack) == 0
        
        