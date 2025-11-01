g={
    'A':{'B','C'},
    
    'B':{'D','E'},
    
    'C':{'F','G'},
    'D':set(),
    'E':set(),
    'F':set(),
    'G':set(),

}
from collections import deque
def b(s,e):
    frontier=deque([s])
    visited={s}
    parent={s:None}
    while frontier:
        n=frontier.popleft()
        if n==e:
            path=[]
            current=e
            while current in not Nonw:
                path.append(current)
                current=parent[current]
            return path[::-1]
        
        for child in g[n]:
            if child not in visited:
                visited.add(child)
                parent[child]=n
                frontier.append(child)




def bfs(s,e,exp=None):
    if exp is None:
        exp=[]
    frontier=[s]
    while frontier:
        n=frontier.pop(0)
        exp.append(n)
        if e in exp:
            return exp
        for child in g[n]:
            if child not in frontier or child not in exp:
                frontier.append(child)


s=input('enter start:').upper()

e=input('enter goal:').upper()



r=bfs(s,e)



print(r)
print(b(s,e))
