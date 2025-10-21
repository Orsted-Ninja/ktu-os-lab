G = {'A':{'B':1,'C':4}, 'B':{'D':2,'E':5}, 'C':{'F':3}, 'D':{'G':3}, 'E':{'G':2}, 'F':{'G':1}, 'G':{}}
H = {'A':7, 'B':5, 'C':4, 'D':3, 'E':2, 'F':1, 'G':0}

def a_star(s, g):
    O = [(H[s], s, [s])]
    c = {s: 0}
    while O:
        O.sort(key=lambda x: x[0])
        f, n, p = O.pop(0)
        if n == g:
            return f - H[n], p
        for k, v in G[n].items():
            t = c[n] + v
            if k not in c or t < c[k]:
                c[k] = t
                O.append((t + H[k], k, p + [k]))
    return None, []

c, p = a_star('A', 'G')
print("PATH", "->".join(p))
print("Cost is ", c)