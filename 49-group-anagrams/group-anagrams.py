class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for str in strs:
            data = [0] * 26

            for ch in str:
                data[ord(ch) - ord('a')] +=1
            map[tuple(data)].append(str)
        return list(map.values())
        #     data = ''.join(sorted(str))

        #     map[data].append(str)
        # return list(map.values())     