class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        max_f = max(f for f, _ in items)
        freq = [0] * (max_f + 1)
        for f, _ in items:
            freq[f] += 1

        # gain[f] = 1 (purchased copy) + count of other items divisible by f
        gain = [0] * (max_f + 1)
        for f in range(1, max_f + 1):
            if freq[f]:
                gain[f] = sum(freq[m] for m in range(f, max_f + 1, f))

        dp = [0] * (budget + 1)
        min_price = min(p for _, p in items)

        # 0/1 Knapsack for first-time purchases (with freebies)
        for f, price in items:
            g = gain[f]
            for b in range(budget, price - 1, -1):
                val = dp[b - price] + g
                if val > dp[b]:
                    dp[b] = val

        # Greedily spend any leftover budget on the cheapest item
        return max(dp[b] + (budget - b) // min_price for b in range(budget + 1))