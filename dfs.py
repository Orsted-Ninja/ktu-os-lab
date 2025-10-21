





global g

g = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F','G'],
    'D': [],
    'E': [],
    'F': [],
    'G': ['H'],
    'H': []
}

def dfs(start, exp=[]):   #s
    exp.append(start)
    for x in g[start]:
        if x not in exp:
            dfs(x, exp)
    return exp    #e

print("Root Node is A:")
print("Sequence:")
print(dfs('A'))


