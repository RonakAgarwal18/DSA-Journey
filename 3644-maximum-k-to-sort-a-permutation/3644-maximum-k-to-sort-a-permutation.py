
class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = 0
        found = False

        for i in range(len(nums)):
            if nums[i] != i:
                if not found:
                    k = nums[i]
                    found = True
                else:
                    k &= nums[i]

        return k
