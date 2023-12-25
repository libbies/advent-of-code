from collections import defaultdict
from igraph import Graph
lines = [l.strip().split(': ') for l in open("input.txt").readlines()]

graph = defaultdict(list)
for node, adjacent in lines:
    for adj in adjacent.split():
        graph[node].append(adj)
        graph[adj].append(node)

graph = Graph.ListDict(graph)
s1, s2 = Graph.mincut(graph).sizes()

answer = s1 * s2
print("aoc 2023 day 25:", answer)
