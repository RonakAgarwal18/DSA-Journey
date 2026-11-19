import heapq

class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        small = heapq.nsmallest(3, nums)  # [min1, min2, min3]
        large = heapq.nlargest(3, nums)   # [max1, max2, max3]
        return min(
            large[0] - small[2],  # Change 2 smallest
            large[1] - small[1],  # Change 1 smallest and 1 largest
            large[2] - small[0],  # Change 2 largest
        )