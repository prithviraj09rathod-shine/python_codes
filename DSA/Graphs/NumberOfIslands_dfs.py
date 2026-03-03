class solution:
    def NumberofIslands(self, grid)->int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if grid[r][c] == '0' or visited[r][c]:
                return
            
            visited[r][c] = True
            
            # Explore all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        island_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    dfs(r, c)
                    island_count += 1
        
        return island_count

# Example usage:
obj = solution()
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print("Number of Islands:", obj.NumberofIslands(grid))  # Output: 3
