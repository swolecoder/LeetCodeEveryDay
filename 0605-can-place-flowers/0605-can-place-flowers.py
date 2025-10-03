class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]


        for i in range(1, len(f)-1):

            if n == 0:
                return True

            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0 and n > 0:
                f[i] = 1
                n -=1 

                if n == 0:
                    return True

        return n <= 0       