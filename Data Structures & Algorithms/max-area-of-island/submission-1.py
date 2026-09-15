class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        0 is water 
        1 is land
        an island defined as groups of 1 connected h or v
        edges are water
        
        """
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0
            else:
                grid[r][c] = 0
                return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c)) #this looks at the max between dfs(r,c) and max_area that was stored, if one of them is bigger, then we store that as the new max_area
        return max_area
                