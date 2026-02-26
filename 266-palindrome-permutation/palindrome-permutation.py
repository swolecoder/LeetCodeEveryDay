class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        seen = set()


        for ch in s:
            if ch in seen:
                seen.remove(ch)
            else:
                seen.add(ch)
        return len(seen) <= 1
        # map = Counter(s)


        # odd = 0

        # for ch, count in map.items():
        #     if count % 2 == 1:
        #         odd +=1

        #         if odd > 1:
        #             return False
        # return True