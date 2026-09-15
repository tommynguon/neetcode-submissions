class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        direction =[[1,0],[-1,0],[0,1],[0,-1]]
        rows = len(grid) #horizontal count
        cols = len(grid[0]) #vertical count cause grid[0] checks how many items in the horizontal count which also would give us amount of cols yk?
        island_count = 0

        def dfs(r,c):
            #setting edge cases cause r cant be less than 0 other wise, it would be ontop of the graph, or if i has to be atleast m then it would be below the graph
            #same idea for j
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            else:
                grid[r][c] = "0"
                dfs(r, c+1)
                dfs(r+1, c)
                dfs(r, c-1)
                dfs(r-1, c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    dfs(r,c)
        
        return island_count



