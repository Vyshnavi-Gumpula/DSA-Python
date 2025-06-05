from collections import defaultdict
def sssp(u,v):
  dis=defaultdict(lambda:float('inf'))
  sp=defaultdict(int)
  sp[u]=u
  dis[u]=0
  q=[u]
  vi=set()
  while(q):
    n=q.pop()
    vi.add(n)
    for i,w in d[n]:
      if(dis[n]+w < dis[i]):
        dis[i]=dis[n]+w
        sp[i]=n
      if(i not in q and i not in vi):
        q.append(i)
  print(dis)
  l=[v]
  while(sp[v]!=v):
    l.append(sp[v])
    v=sp[v]
  print(l[::-1])  
a = [(10,5,2) , (10,7,4) , (5,7,1) , (5,8,3) , (7,8,1) , (5,3,2) , (8,3,1)]
d = defaultdict(list)
for i,j,w in a :
  d[i].append([j,w])
  d[j].append([i,w])
print(d)
sssp(10,8)