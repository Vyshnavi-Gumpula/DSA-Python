from collections import defaultdict
def print_all_paths(u,v,path=[]):
    path.append(u)
    if u==v:
        print(path)
    for i,w in d[u]:
        if i not in path:
            print_all_paths(i,v,path)
    path.pop()
    return
a=[(5,2,3),(5,7,2),(5,8,1),(2,7,2),(2,8,4),(8,7,1),(8,3,3),(2,3,2)]
d=defaultdict(list)
for i,j,w in a:
    d[i].append([j,w])
    d[j].append([i,w])
print(d)
print_all_paths(5,3)
# printing cost
from collections import defaultdict
def cost_all_paths(u,v,path=[],cost=0):
    path.append(u)
    if u==v:
        print(path,cost)
    for i,w in d[u]:
        if i not in path:
            cost=cost+w
            cost_all_paths(i,v,path,cost)
            cost=cost-w
    path.pop()
    return
a=[(5,2,3),(5,7,2),(5,8,1),(2,7,2),(2,8,4),(8,7,1),(8,3,3),(2,3,2)]
d=defaultdict(list)
for i,j,w in a:
    d[i].append([j,w])
    d[j].append([i,w])
print(d)
cost_all_paths(5,3)