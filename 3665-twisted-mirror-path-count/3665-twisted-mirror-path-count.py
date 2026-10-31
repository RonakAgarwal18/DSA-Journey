class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        cols = len(grid[0])
        down = [0] * cols
        down[0] = 1
        
        for row in grid:
            right = 0
            for c, cell in enumerate(row):
                if cell == 0:
                    right = down[c] = (right + down[c]) % MOD
                else:
                    right, down[c] = down[c], right
                    
        return down[-1]