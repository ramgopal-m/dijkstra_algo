def dfs(g, s, vis=None):
    if vis is None:
        vis = set()
    print(s, end=' ')
    vis.add(s)

    for nei in g[s]:
        if nei not in vis:
            dfs(g, nei, vis)

g = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'E'],
    'D': ['A', 'E'],
    'E': ['B', 'C', 'D']
}

print("DFS from A:")
dfs(g, 'A')
