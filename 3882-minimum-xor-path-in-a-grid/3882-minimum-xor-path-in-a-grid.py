class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [set() for _ in range(cols)]
        dp[0].add(0)
        
        for r in range(rows):
            for c in range(cols):
                val = grid[r][c]
                if c > 0:
                    dp[c].update(dp[c - 1])
                dp[c] = {x ^ val for x in dp[c]}
                
        return min(dp[-1])