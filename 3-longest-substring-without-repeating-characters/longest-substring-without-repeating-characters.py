class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = 0
        i =0

        for r in range(len(s)):

            while s[r] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[r])
            ans  =max(ans, r-i +1)
        return ans