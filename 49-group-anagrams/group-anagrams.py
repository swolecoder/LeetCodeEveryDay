class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for str in strs:
            data = ''.join(sorted(str))

            map[data].append(str)
        return list(map.values())     