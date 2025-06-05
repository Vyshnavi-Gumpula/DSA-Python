from collections import defaultdict
import heapq
def prims(u):
    vi=set()
    sp=[]
    cost=0
    q=[(0,u,-1)]
    while q:
        w,n,p = heapq.heappop(q)
        if n in vi:
            continue
        vi.add(n)
        if p!=-1:            
            sp.append((p,n,w))
        cost += w
        for i, wt in d[n]:
            if i not in vi:
                heapq.heappush(q,(wt,i,n))
    print(cost)
    print(sp)
a=[(10,5,2),(10,7,4),(5,7,1),(5,8,3),(7,8,1),(5,3,2),(8,3,1),(8,9,2)]
d=defaultdict(list)
for i,j,w in a :
  d[i].append([j,w])
  d[j].append([i,w])
print(d)
prims(10)
