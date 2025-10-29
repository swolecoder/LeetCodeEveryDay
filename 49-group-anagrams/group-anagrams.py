class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = {}
        

        for str in strs:
            data = sorted(str)
            found = ''.join(data)

            if found not in map:
                map[found] = []
            map[found].append(str)

        print(map)
        return list(map.values())
