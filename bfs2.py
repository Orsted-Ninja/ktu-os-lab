G = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def bfs_path(graph, start, goal):
    # Keep track of explored nodes to avoid cycles
    explored = set()
    # Queue of paths to explore
    queue = [[start]]

    # Return path if start is goal
    if start == goal:
        return [start]
    
    # Loop until the queue is empty
    while queue:
        # Get the first path from the queue
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbors = graph.get(node, [])
            # Go through all neighbor nodes
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                # Return path if neighbor is goal
                if neighbor == goal:
                    return new_path

            # Mark the node as explored
            explored.add(node)
    
    # If the queue is empty and goal not found, return None
    return None

start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

# Convert input to uppercase to match graph keys
shortest_path = bfs_path(G, start_node.upper(), goal_node.upper())

if shortest_path:
    print("\nShortest path found:")
    print(' -> '.join(shortest_path))
else:
    print(f"\nNo path found from {start_node.upper()} to {goal_node.upper()}.")

