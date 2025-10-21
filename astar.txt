




def a_star_search(graph, heuristic, start, goal):

    visited = set()

    to_visit = {start: heuristic[start]} 

    g_cost = {start: 0}

    parent = {start: start}


    while to_visit:

        current = min(to_visit, key=to_visit.get)

        

        if current == goal:

            path = []

            total_cost = g_cost[current]

            while parent[current] != current:

                path.append(current)

                current = parent[current]

            path.append(start)

            path.reverse()

            print("Path found:", " -> ".join(path))

            print(f"Total cost: {total_cost}")

            return path


        to_visit.pop(current)

        visited.add(current)

        

        for neighbor, cost in graph.get(current, {}).items():

            if neighbor in visited:

                continue

            

            tentative_g = g_cost[current] + cost

            

            if tentative_g < g_cost.get(neighbor, float('inf')):

                parent[neighbor] = current

                g_cost[neighbor] = tentative_g

                f_cost = tentative_g + heuristic[neighbor]

                to_visit[neighbor] = f_cost

                

    print("Path does not exist.")

    return None


graph = {}

heuristic = {}


v = int(input("Enter the number of vertices: "))

print("\n--- Define Nodes and Heuristics ---")

for i in range(v):

    node = input(f"Enter vertex #{i+1}: ")

    heur_val = int(input(f"Enter heuristic value for {node}: "))

    graph[node] = {}

    heuristic[node] = heur_val


e = int(input("\nEnter the total number of edges: "))

print("\n--- Define Edges and Costs ---")

for _ in range(e):

    edge_input = input("Enter edge and cost (format: V1 V2 cost): ").split()

    v1, v2, cost = edge_input[0], edge_input[1], int(edge_input[2])

    if v1 in graph and v2 in graph:

        graph[v1][v2] = cost

        graph[v2][v1] = cost

    else:

        print(f"Warning: One or both vertices ({v1}, {v2}) not defined. Skipping edge.")


start = input("\nEnter the start vertex: ")

goal = input("Enter the goal vertex: ")


if start not in graph or goal not in graph:

    print("Error: Start or goal node not present in the graph.")

else:

    print("\n--- A* Search ---")

    a_star_search(graph, heuristic, start, goal)





