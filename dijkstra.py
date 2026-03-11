#!/usr/bin/env python3
"""Dijkstra's shortest path. Input: 'src dst weight' per line."""
import sys, heapq, collections
g = collections.defaultdict(list)
for line in sys.stdin:
    parts = line.strip().split()
    if len(parts) >= 3:
        u, v, w = parts[0], parts[1], float(parts[2])
        g[u].append((v, w)); g[v].append((u, w))
src = sys.argv[1] if len(sys.argv) > 1 else next(iter(g))
dst = sys.argv[2] if len(sys.argv) > 2 else None
dist, prev = {src: 0}, {}
pq = [(0, src)]
while pq:
    d, u = heapq.heappop(pq)
    if d > dist.get(u, float('inf')): continue
    for v, w in g[u]:
        nd = d + w
        if nd < dist.get(v, float('inf')):
            dist[v] = nd; prev[v] = u; heapq.heappush(pq, (nd, v))
if dst and dst in dist:
    path, n = [], dst
    while n in prev: path.append(n); n = prev[n]
    path.append(src)
    print(f"{' → '.join(reversed(path))} (cost: {dist[dst]})")
else:
    for n in sorted(dist): print(f"{src} → {n}: {dist[n]}")
