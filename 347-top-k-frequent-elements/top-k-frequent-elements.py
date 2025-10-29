class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = defaultdict(int)

        for num in nums:
            map[num] +=1
        
        h = [(v, key) for key, v in map.items()]
        # print(h)
        heapq.heapify(h)

        while len(h) > k:
            heapq.heappop(h)
    

        print(h)

        ans = [num for (freq, num) in h]

        return ans

        