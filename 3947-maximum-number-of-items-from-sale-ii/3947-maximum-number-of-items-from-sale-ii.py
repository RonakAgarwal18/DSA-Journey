class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        min_price = min(p for _, p in items)
        
        freq = [0] * (n + 1)
        for f, _ in items:
            freq[f] += 1
            
        # mult[f] = total items whose factor is divisible by f
        mult = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f]:
                mult[f] = sum(freq[m] for m in range(f, n + 1, f))
                
        # Keep only useful bonus items (worth 2 copies each)
        limit = 2 * min_price
        candidates = []
        for f, price in items:
            cap = mult[f] - 1
            if cap > 0 and price < limit:
                candidates.append((price, cap))
                
        candidates.sort()
        
        ans = 0
        for price, cap in candidates:
            if budget < price:
                break
            take = min(cap, budget // price)
            ans += 2 * take
            budget -= take * price
            
        # Spend any remaining budget on plain copies of the cheapest item
        return ans + budget // min_price