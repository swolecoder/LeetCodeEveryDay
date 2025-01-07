from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for str in strs:
            data = [0] * 26

            for i in range(len(str)):
                data[ord(str[i]) - ord('a')] +=1
            map[tuple(data)].append(str)
        return list(map.values())

        