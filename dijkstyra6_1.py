def dijkstra(g, s, e):
    vis = set()
    dist = {n: float('inf') for n in g}
    dist[s] = 0
    prev = {s: None}

    while len(vis) < len(g):
        u = None
        for n in g:
            if n not in vis and (u is None or dist[n] < dist[u]):
                u = n

        if u is None:
            break

        vis.add(u)

        for v, w in g[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
    path = []
    cur = e
    while cur:
        path.append(cur)
        cur = prev[cur]
    path.reverse()

    return dist[e], path

g = {
    'A': [('B', 6), ('D', 1)],
    'B': [('A', 6), ('C', 5), ('E', 2)],
    'C': [('B', 5), ('E', 5)],
    'D': [('A', 1), ('E', 1)],
    'E': [('B', 2), ('C', 5), ('D', 1)]
}

d, p = dijkstra(g, 'A', 'C')

print("Dist:", d)
print("Path:", ' -> '.join(p))
