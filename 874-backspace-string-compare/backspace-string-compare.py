class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def convert(d):
            stack = []

            for ch in d:
                if ch == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return ''.join(stack)


        return convert(s) == convert(t)
        