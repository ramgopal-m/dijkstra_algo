def color_graph(g):
    col = {}  

    for n in g:
        used = {col[v] for v in g[n] if v in col} 
        for c in range(1, 4):
            if c not in used:
                col[n] = c
                break

    return col

g = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'E'],
    'D': ['A', 'E'],
    'E': ['B', 'C', 'D']
}

colors = color_graph(g)
for n in colors:
    print(f"Node {n} → Color {colors[n]}")
