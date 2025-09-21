class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i, t in enumerate(temperatures):
            print(i, t)

            while stack and t > temperatures[stack[-1]]:
                prev = stack.pop()
                print(prev)
                ans[prev] = i - prev
            stack.append(i)
        return ans