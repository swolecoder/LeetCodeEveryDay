class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        arr = []
        print(count)

        for val in count.keys():
            arr.append((count[val], val))
        
        print(arr)
        arr.sort()

        ans = []
        print("Ashish")
        print(arr)

        while len(arr) > 0 and k >0:
            ans.append(arr[-1][1])
            arr.pop()
            k -=1
            print(k)
        return ans