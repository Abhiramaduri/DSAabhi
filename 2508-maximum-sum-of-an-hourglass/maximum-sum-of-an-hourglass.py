class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        max_total = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows - 2):
            for c in range(cols - 2):
                current_sum = (
                    grid[r][c] + grid[r][c+1] + grid[r][c+2] + 
                    grid[r+1][c+1] +                            
                    grid[grid_r:=r+2][c] + grid[grid_r][c+1] + grid[grid_r][c+2] 
                )
                
                if current_sum > max_total:
                    max_total = current_sum
                    
        return max_total
