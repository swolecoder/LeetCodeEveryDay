class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # ans = ""

        # for i in range(len(strs[0])):
        #     for word in strs:
        #         if  i == len(word) or word[i] != strs[0][i]:
        #             return ans
            
        #     ans += strs[0][i]
        # return ans

        def common(length):

            common = strs[0][:length]

            return all( word.startswith(common) for word in strs)


        l = 0 
        r = min(len(s) for s in strs)

        while l < r:


            mid = ( l +r +1)//2

            if common(mid):
                l = mid 
            else:
                r = mid -1
        
        return strs[0][:l]
        


        