class Solution:
    def calPoints(self, operations: List[str]) -> int:

        s = []

        for o in operations:
            if o == 'C':
                s.pop()
            elif o == "D":
                s.append(s[-1] * 2)
            elif o == "+":
                s.append(s[-1] + s[-2])
            else:
                s.append(int(o))
        print(s)
        return 0 if not s else sum(s)

        