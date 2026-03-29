from dijkstra import WeightedGraph
g = WeightedGraph()
g.add_edge("A","B",4); g.add_edge("A","C",2); g.add_edge("C","B",1); g.add_edge("B","D",3); g.add_edge("C","D",5)
path, dist = g.shortest_path("A", "D")
assert dist == 6  # A->C->B->D = 2+1+3
assert path == ["A","C","B","D"]
path2, dist2 = g.shortest_path("A", "A")
assert dist2 == 0
path3, dist3 = g.shortest_path("A", "Z")
assert path3 is None
dists, _ = g.dijkstra("A")
assert dists["C"] == 2
assert dists["B"] == 3
print("dijkstra tests passed")
