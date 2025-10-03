class Solution:
    def maxDifference(self, s: str) -> int:
        map = Counter(s)

        odd= [v for k, v in map.items() if v % 2 == 1]
        even = [v for k,v in map.items() if v %2 == 0]

        if not odd or not even:
            return -1

        return max(odd) - min(even)
        