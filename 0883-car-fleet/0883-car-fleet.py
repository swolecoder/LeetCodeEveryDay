class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        data = [(p,s) for p,s in zip(position,speed)]
        stack = []
        data = sorted(data,reverse=True)
        print(data)

        for pos,sp in data:
            time = (target-pos)/sp

            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)


        