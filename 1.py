from collections import defaultdict
with open("in.txt") as file:
    N = int(file.readline())
    pred = []
    for i in range(N):
        s = []
        ss = file.readline().split()[:-1]
        for j in range(0,len(ss),2):
            s.append((int(ss[j]), int(ss[j+1])))
        pred.append(s)
    vv = int(file.readline())
    ww = int(file.readline())

gr =defaultdict(set)
c = defaultdict(dict)
for i in range(N):
    for j in pred[i]:
        gr[j[0]].add(i+1)
        c[j[0]][i+1]=j[1]
n = N
numbers = [-1 for i in range(N)]
deleted = set()
all = {i for i in range(1,N+1)}
while len(deleted)<N:
    for i in all.difference(deleted):
        if gr[i].issubset(deleted):
            numbers[i-1]=n
            n-=1
            deleted.add(i)
prev = {}
d = {}
for i in range(1, N+1):
    prev[i] = 0
    d[i] =-99999999999999
d[vv]=0
for k in range(vv,ww+1):
    for v in gr[k]:
        if d[k]>=0 and d[k] + c[k][v]>d[v]:
            d[v] = d[k]+ c[k][v]
            prev[v]=k

with open("out.txt", "w") as file:
    if d[ww]>=0:

        path = [ww]
        while path[-1] != vv:
            path.append(prev[path[-1]])
        file.write("Y\n")
        file.write(" ".join([str(i) for i in path[::-1]]))
        file.write("\n"+str(d[ww]))
    else:
        file.write("N")
