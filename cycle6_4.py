def has_cycle(g):
    def dfs(u, p):
        vis.add(u)
        for v in g[u]:
            if v not in vis:
                if dfs(v, u):
                    return True
            elif v != p:
                return True
        return False

    vis = set()
    for node in g:
        if node not in vis:
            if dfs(node, None):
                return True
    return False

# Graph with a cycle
g = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'E'],
    'D': ['A', 'E'],
    'E': ['B', 'C', 'D']
}

if has_cycle(g):
    print("Cycle Detected")
else:
    print("No Cycle")
