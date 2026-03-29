#!/usr/bin/env python3
"""Dijkstra shortest path algorithm. Zero dependencies."""
import heapq

class WeightedGraph:
    def __init__(self, directed=False):
        self.adj = {}
        self.directed = directed

    def add_edge(self, u, v, weight):
        self.adj.setdefault(u, []).append((v, weight))
        if not self.directed:
            self.adj.setdefault(v, []).append((u, weight))

    def dijkstra(self, start):
        dist = {start: 0}
        prev = {start: None}
        heap = [(0, start)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist.get(u, float("inf")): continue
            for v, w in self.adj.get(u, []):
                nd = d + w
                if nd < dist.get(v, float("inf")):
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(heap, (nd, v))
        return dist, prev

    def shortest_path(self, start, end):
        dist, prev = self.dijkstra(start)
        if end not in dist: return None, float("inf")
        path = []
        node = end
        while node is not None:
            path.append(node)
            node = prev[node]
        return list(reversed(path)), dist[end]

    def all_pairs(self):
        result = {}
        for node in self.adj:
            result[node] = self.dijkstra(node)[0]
        return result

if __name__ == "__main__":
    g = WeightedGraph()
    g.add_edge("A","B",4); g.add_edge("A","C",2); g.add_edge("C","B",1)
    path, dist = g.shortest_path("A", "B")
    print(f"A->B: {path} (dist={dist})")
