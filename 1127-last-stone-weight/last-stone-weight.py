from heapq import heappush, heappop,heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        h = [ -s for s in stones]
        heapify(h)

        while len(h) > 1:

            f = heappop(h)
            s = heappop(h)

            diff = abs(f-s)

            if diff:
                heappush(h,-diff)
        

        return -h[0] if len(h) >0 else 0
            
        