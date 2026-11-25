import random

class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        MOD = (1 << 61) - 1
        BASE = random.randint(100001, 10**9)

        # Precompute prefix hashes once in O(n)
        H = [0] * (n + 1)
        for i, x in enumerate(nums):
            H[i + 1] = (H[i] * BASE + x) % MOD

        def has_unique(length: int) -> bool:
            p = pow(BASE, length, MOD)
            seen = set()
            dups = set()
            for i in range(n - length + 1):
                h = (H[i + length] - H[i] * p) % MOD
                if h in seen:
                    dups.add(h)
                else:
                    seen.add(h)
            return len(seen) > len(dups)

        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if has_unique(mid):
                right = mid
            else:
                left = mid + 1

        return left