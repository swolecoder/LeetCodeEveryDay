class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        ans = 0

        def dfs(r,c):

            if not(0 <= r < len(grid)) or not (0<= c < len(grid[0])) or grid[r][c] != 1:
                return 0
            
            grid[r][c] = "#"
            count = 1

            count  += dfs(r+1,c)
            count  += dfs(r-1,c)
            count  += dfs(r,c-1)
            count  += dfs(r,c+1)

            return count 


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans,dfs(i,j))






        return ans
        