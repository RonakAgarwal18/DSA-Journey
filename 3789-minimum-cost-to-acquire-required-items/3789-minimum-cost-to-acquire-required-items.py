class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Case 1: Buy only individual items
        case1 = need1 * cost1 + need2 * cost2
        
        # Case 2: Buy only bundle items to cover both requirements
        case2 = max(need1, need2) * costBoth
        
        # Case 3: Buy bundles for the shared part, singles for the rest
        mn = min(need1, need2)
        case3 = mn * costBoth + (need1 - mn) * cost1 + (need2 - mn) * cost2
        
        return min(case1, case2, case3)