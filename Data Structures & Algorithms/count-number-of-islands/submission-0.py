class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        def dfs(ROWS,COLS):
            if ROWS<0 or ROWS>=rows or COLS<0 or COLS>=cols or grid[ROWS][COLS]=='0':
                return
            grid[ROWS][COLS]='0'
            dfs(ROWS+1,COLS)
            dfs(ROWS,COLS+1)
            dfs(ROWS-1,COLS)
            dfs(ROWS,COLS-1)


        rows=len(grid)
        cols=len(grid[0])
        islands=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    islands+=1
                    dfs(r,c)
        return islands