import random

def pr(color):
    print("Solution found:")
    for i in range(4):
        print(color[i])

def Safe(g, color):
    for i in range(4):
        for j in range(i + 1, 4):
            if g[i][j] == 1 and color[j] == color[i]:
                return False
    return True

def gmc(g, m, color):
    max_steps = 1000

    for _ in range(max_steps):
        if Safe(g, color):
            pr(color)
            return True

        conflicted_nodes = []
        for i in range(4):
            for j in range(i + 1, 4):
                if g[i][j] == 1 and color[i] == color[j]:
                    conflicted_nodes.append(i)
                    conflicted_nodes.append(j)
        
        if not conflicted_nodes:
            continue
            
        i = random.choice(list(set(conflicted_nodes)))

        min_conflicts = 5
        best_color = color[i]
        
        for j in range(1, m + 1):
            color[i] = j
            current_conflicts = 0
            
            for k in range(4):
                if g[i][k] == 1 and color[i] == color[k]:
                    current_conflicts += 1
            
            if current_conflicts < min_conflicts:
                min_conflicts = current_conflicts
                best_color = j

        color[i] = best_color

    return False

g = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
m = 3

color = [random.randint(1, m) for i in range(4)]

print(f"Starting with random assignment: {color}")

if gmc(g, m, color):
    print('yes')
else:
    print('no solution found')
