class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minHeap = []
        trips.sort(key = lambda t:t[1])
        c = 0

        for trip in trips:
            p, s, e = trip

            while minHeap and minHeap[0][0] <= s:
                c -= minHeap[0][1]
                heapq.heappop(minHeap)  
            c += p
            if c > capacity:
                return False
            heapq.heappush(minHeap,(e,p))
        return True

