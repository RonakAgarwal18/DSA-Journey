from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = deque()  # Stores [roof_value, count_of_elements]
        r = n - 1
        cost = 0
        ans = 0
        
        for l in range(n - 1, -1, -1):
            v = nums[l]
            cnt = 1
            
            while q and q[0][0] <= v:
                val, c = q.popleft()
                cost += (v - val) * c
                cnt += c
            q.appendleft([v, cnt])
            
            while cost > k:
                cost -= q[-1][0] - nums[r]
                q[-1][1] -= 1
                if q[-1][1] == 0:
                    q.pop()
                r -= 1
                
            ans += r - l + 1
            
        return ans