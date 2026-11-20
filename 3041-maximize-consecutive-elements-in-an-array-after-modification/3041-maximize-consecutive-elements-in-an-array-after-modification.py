class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()
        ans = 1
        dp0 = dp1 = 0
        prev = -10  # Anything < min(nums) - 2
        
        for x in nums:
            if x == prev:
                dp1 = dp0 + 1
            elif x == prev + 1:
                dp0 += 1
                dp1 += 1
            elif x == prev + 2:
                dp0 = dp1 + 1
                dp1 = 1
            else:
                dp0 = dp1 = 1
                
            prev = x
            if dp0 > ans:
                ans = dp0
            if dp1 > ans:
                ans = dp1
                
        return ans