g = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': ['H'],
    'H': []
}

def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]

    if start == goal:
        return path

    if start not in graph:
        return None

    for node in graph[start]:
        if node not in path:
            new_path = dfs(graph, node, goal, path)
            if new_path:
                return new_path
                
    return None

start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

path_to_goal = dfs(g, start_node.upper(), goal_node.upper())

if path_to_goal:
    print("\nPath found:")
    print(' -> '.join(path_to_goal))
else:
    print(f"\nNo path found from {start_node.upper()} to {goal_node.upper()}.")
