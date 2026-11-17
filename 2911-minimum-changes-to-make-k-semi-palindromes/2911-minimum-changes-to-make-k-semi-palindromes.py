class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # 1. Precompute valid divisors d (1 <= d < L) for every length L
        divs = [[] for _ in range(n + 1)]
        for d in range(1, n + 1):
            for L in range(d * 2, n + 1, d):
                divs[L].append(d)
                
        # 2. Precompute cost[i][j]: min changes to make s[i..j] a semi-palindrome
        cost = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                for d in divs[L]:
                    changes = 0
                    for offset in range(d):
                        left = i + offset
                        right = j - d + 1 + offset
                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d
                    if changes < cost[i][j]:
                        cost[i][j] = changes
                        
        # 3. Partition DP: split s into k semi-palindromes
        dp = cost[0][:]  # Base case (1 partition): cost of s[0..j]
        for p in range(2, k + 1):
            new_dp = [float('inf')] * n
            for j in range(2 * p - 1, n):
                best = float('inf')
                for prev in range(2 * (p - 1) - 1, j - 1):
                    if dp[prev] + cost[prev + 1][j] < best:
                        best = dp[prev] + cost[prev + 1][j]
                new_dp[j] = best
            dp = new_dp
            
        return dp[n - 1]