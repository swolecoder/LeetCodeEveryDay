class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        map = Counter(s)


        odd = 0

        for ch, count in map.items():
            if count % 2 == 1:
                odd +=1

                if odd > 1:
                    return False
        return True