from heapq import heappush, heappop

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        inf = float('inf')
        dist = [{} for _ in range(n)]
        dist[0][1] = 0
        min_cnt = [k + 1] * n
        
        pq = [(0, 0, 1)]  # (cost, node, consecutive_count)
        
        while pq:
            cost, u, cnt = heappop(pq)
            
            if u == n - 1:
                return cost
                
            if cnt >= min_cnt[u]:
                continue
            min_cnt[u] = cnt
            
            u_label = labels[u]
            for v, w in adj[u]:
                nc = cnt + 1 if labels[v] == u_label else 1
                if nc < min_cnt[v]:
                    new_cost = cost + w
                    if new_cost < dist[v].get(nc, inf):
                        dist[v][nc] = new_cost
                        heappush(pq, (new_cost, v, nc))
                        
        return -1