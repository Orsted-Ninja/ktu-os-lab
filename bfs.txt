g = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def bfs(g, s):
    frontier = [s]
    explored = []

    while frontier != []:
        n = frontier.pop(0)
        explored.append(n)

        for child in g[n]:
            if child not in explored and child not in frontier:
                frontier.append(child)
    return explored

result = bfs(g, 'A')
print(f"The sequence is: {result}")



The sequence is: ['A', 'B', 'C', 'D', 'E', 'F', 'G']