#!/usr/bin/env python3
"""dijkstra - Dijkstra's shortest path algorithm."""
import sys,heapq,json
def dijkstra(graph,src):
    dist={v:float('inf') for v in graph};dist[src]=0;prev={};pq=[(0,src)]
    while pq:
        d,u=heapq.heappop(pq)
        if d>dist[u]:continue
        for v,w in graph.get(u,[]):
            nd=d+w
            if nd<dist[v]:dist[v]=nd;prev[v]=u;heapq.heappush(pq,(nd,v))
    return dist,prev
def path(prev,dst):
    p=[];n=dst
    while n in prev:p.append(n);n=prev[n]
    p.append(n);return list(reversed(p))
if __name__=="__main__":
    graph={"A":[("B",4),("C",2)],"B":[("D",3),("C",1)],"C":[("B",1),("D",5)],"D":[("E",1)],"E":[]}
    src="A";dist,prev=dijkstra(graph,src)
    for v in sorted(dist):p=path(prev,v) if v in prev or v==src else[v];print(f"  {src}→{v}: {dist[v]} via {' → '.join(p)}")
