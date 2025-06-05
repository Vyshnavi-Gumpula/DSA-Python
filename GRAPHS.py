#Graphs
from collections import defaultdict
def print_all_paths(u,v,path=[]):
    path.append(u)
    if u==v:
        print(path)
        path.pop()
        return 
    for i in d[u]:
        if i not in path:
            print_all_paths(i,v,path)
    path.pop()
    return 
graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
d=defaultdict(list)
for i,j in graphs:
    d[i].append(j)
    d[j].append(i)
print(d)
print_all_paths(5,3)
#count the paths
from collections import defaultdict
def print_all_paths(u,v,path=[],c=0):
    path.append(u)
    if u==v:
        c+=1
    for i in d[u]:
        if i not in path:
            c=print_all_paths(i,v,path,c)
    path.pop()
    return c 
graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
d=defaultdict(list)
for i,j in graphs:
    d[i].append(j)
    d[j].append(i)
print(d)
print(print_all_paths(5,3))
#or
from collections import defaultdict
def print_all_paths(u,v,path=set(),c=0):
    path.add(u)
    if u==v:
        c+=1
    for i in d[u]:
        if i not in path:
            c=print_all_paths(i,v,path,c)
    path.remove(u)
    return c 
graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
d=defaultdict(list)
for i,j in graphs:
    d[i].append(j)
    d[j].append(i)
print(d)
print(print_all_paths(5,3))
#or
from collections import defaultdict
def print_all_paths(u,v,path=[],c=0):
    path.append(u)
    if u==v:
        print(path,c+1)
    for i in d[u]:
        if i not in path:
            c+=1
            print_all_paths(i,v,path,c)
            c-=1
    path.pop()
    return 
graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
d=defaultdict(list)
for i,j in graphs:
    d[i].append(j)
    d[j].append(i)
print(d)
print_all_paths(5,3)

#path is there or not
from collections import defaultdict
def check_if_paths(u,v,path=[]):
    path.append(u)
    if u==v:
        return True
    else:
        for i in d[u]:
            if i not in path:
                if check_if_paths(i,v,path):
                    return True
    path.pop()
    return False
graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
d=defaultdict(list)
for i,j in graphs:
    d[i].append(j)
    d[j].append(i)
print(d)
print(check_if_paths(5,3))
#BFS
#printing all the nodes using BFS
from collections import defaultdict
def print_all_nodes(u):
    v=set()
    q=[u]
    while(q):
        curr=q.pop(0)
        print(curr)
        for i in d[curr]:
            if i not in v and i not in q:
                q.append(i)
        v.add(curr)
graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
d=defaultdict(list)
for i,j in graphs:
    d[i].append(j)
    d[j].append(i)
print_all_nodes(5)

#check if path exist or not using BFS
from collections import defaultdict
def check_if_path(u,v):
    vi=set()
    q=[u]
    while(q):
        curr=q.pop(0)
        if curr==v:
            return True
        for i in d[curr]:
            if i not in vi and i not in q:
                q.append(i)
        vi.add(curr)
    return False
graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
d=defaultdict(list)
for i,j in graphs:
    d[i].append(j)
    d[j].append(i)
print(check_if_path(5,3))