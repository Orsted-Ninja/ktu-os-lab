G={
'A':{'B','C'},
'B':{'D','E'},
'C':{'F'},
'D':{'G'},
'E':{'G'},
'F':{'G'},
'G':{}
}
H={
'A':7,
'B':5,
'C':4,
'D':3,
'E':2,
'F':1,
'G':0}
def A(s,e):
	O=[(H[s],s,[s])]
	visited=set()
	while O:
		O.sort(key=lambda x:x[0])
		
		f,n,p=O.pop(0)
		if n not in visited:
			visited.add(n)
		if n==e:
			return p
		for k in G[n]:
			if k not in visited:
				
				O.append((H[k],k,p+[k]))	
s='A'
e='G'
p=A(s,e)

print(p)
