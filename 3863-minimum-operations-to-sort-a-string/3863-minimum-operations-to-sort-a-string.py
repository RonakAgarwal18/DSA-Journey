class Solution:
    def minOperations(self, s: str) -> int:
        r = len(s)
        if all(s[i] <= s[i + 1] for i in range(r - 1)):
            return 0
        if r == 2:
            return -1
        mr = min(s)
        mx = max(s)
        if s[0] == mr or s[-1] == mx:
            return 1
        if any(c == mr or c == mx for c in s[1:-1]):
            return 2
        return 3