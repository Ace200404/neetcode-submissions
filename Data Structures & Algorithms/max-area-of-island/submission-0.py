class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(ROWS,COLS):
            if ROWS<0 or ROWS>=rows or COLS<0 or COLS>=cols or grid[ROWS][COLS]==0:
                return 0
            grid[ROWS][COLS]=0
            
            return 1+dfs(ROWS+1,COLS)+dfs(ROWS,COLS+1)+dfs(ROWS-1,COLS)+dfs(ROWS,COLS-1)


        rows=len(grid)
        cols=len(grid[0])
        maxIsland=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]== 1:
                    maxIsland=max(maxIsland,dfs(r,c))
        return maxIsland