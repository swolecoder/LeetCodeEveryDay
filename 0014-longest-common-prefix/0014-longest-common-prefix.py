class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        n = strs[0]
        res = ""
        for i in range(len(n)):

            for str in strs:
                if i == len(str) or str[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
        