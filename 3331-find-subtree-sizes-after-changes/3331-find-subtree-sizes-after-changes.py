import sys

class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)
        sys.setrecursionlimit(max(2000, n + 500))
        
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
            
        ans = [1] * n
        last = [-1] * 26
        
        def dfs(u: int, p: int) -> None:
            c = ord(s[u]) - 97
            prev = last[c]
            last[c] = u
            
            for v in children[u]:
                dfs(v, u)
                
            last[c] = prev
            target = prev if prev != -1 else p
            if target != -1:
                ans[target] += ans[u]
                
        dfs(0, -1)
        return ans