class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        order = []
        stack = [0]
        
        while stack:
            u = stack.pop()
            order.append(u)
            tin[u] = len(order)
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append(v)
                    
        sz = [1] * n
        heavy = [-1] * n
        for u in reversed(order):
            for v in adj[u]:
                if v != parent[u]:
                    sz[u] += sz[v]
                    if heavy[u] == -1 or sz[v] > sz[heavy[u]]:
                        heavy[u] = v
                        
        head = list(range(n))
        for u in order:
            if heavy[u] != -1:
                head[heavy[u]] = head[u]
                
        bit = [0] * (n + 2)
        
        def update_subtree(u: int, diff: int) -> None:
            i = tin[u]
            while i <= n:
                bit[i] ^= diff
                i += i & -i
            i = tin[u] + sz[u]
            while i <= n:
                bit[i] ^= diff
                i += i & -i
                
        def query_root_xor(u: int) -> int:
            res = 0
            i = tin[u]
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res
            
        masks = [1 << (ord(c) - 97) for c in s]
        for u in range(n):
            update_subtree(u, masks[u])
            
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_mask = 1 << (ord(parts[2]) - 97)
                update_subtree(u, masks[u] ^ new_mask)
                masks[u] = new_mask
            else:
                u, v = int(parts[1]), int(parts[2])
                a, b = u, v
                while head[a] != head[b]:
                    if depth[head[a]] < depth[head[b]]:
                        a, b = b, a
                    a = parent[head[a]]
                lca = a if depth[a] < depth[b] else b
                
                path_mask = query_root_xor(u) ^ query_root_xor(v) ^ masks[lca]
                ans.append((path_mask & (path_mask - 1)) == 0)
                
        return ans