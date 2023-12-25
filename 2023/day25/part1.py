from igraph import Graph
lines = [l.strip().split(': ') for l in open("input.txt").readlines()]

graph = dict()
for node, adjacent in lines:
    graph[node] = adjacent.split()

graph = Graph.ListDict(graph)
s1, s2 = Graph.mincut(graph).sizes()

answer = s1 * s2
print("aoc 2023 day 25:", answer)
