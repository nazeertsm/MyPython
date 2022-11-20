import random
import networkx as nx
import matplotlib.pyplot as plt


def get_paths(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = get_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


petersen = {
    1: [2, 5, 6], 2: [3, 1, 7], 3: [4, 2, 8], 4: [5, 3, 9], 5: [1, 4, 10],
    6: [1, 8, 9], 7: [2, 9, 10], 8: [3, 10, 6], 9: [4, 6, 7], 10: [5, 7, 8],
}

for i in petersen:
    petersen[i].append(-1)
    petersen[i].append(-2)
petersen[-1] = list(range(1, 11))
petersen[-2] = list(range(1, 11))

hamilton_paths = [path[1:-1] for path in get_paths(petersen, -1, -2) if len(path) == len(petersen)]
hamilton_path = random.choice(hamilton_paths)

g = nx.Graph()
for k, vs in petersen.items():
    for v in vs:
        if v in [-1, -2] or k in [-1, -2]:
            continue
        if abs(hamilton_path.index(k) - hamilton_path.index(v)) == 1:
            g.add_edge(k, v, color='blue', width=1.5)
        else:
            g.add_edge(k, v, color='red', width=0.5)

pos = nx.circular_layout(g)
edges = g.edges()
colors = [g[u][v]['color'] for u, v in edges]
widths = [g[u][v]['width'] for u, v in edges]

nx.draw_shell(g, nlist=[range(6, 11), range(1, 6)], edge_color=colors, width=widths)

plt.axis('off')
plt.show()