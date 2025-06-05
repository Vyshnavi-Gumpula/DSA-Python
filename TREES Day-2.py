#inserting nodes in bst
class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def inorder(self,root):
        if(root==None):
            return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
    def preorder(self,root):
        if root==None:
            return
        print(root.data,end=" ")
        self.inorder(root.left)
        self.inorder(root.right)
    def postorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        self.inorder(root.right)
        print(root.data,end=" ")
def height(root):
    if root==None:
        return -1
    return max(height(root.left),height(root.right))+1
def insert(root,x):
    if root==None:
        return node(x)
    if x<root.data:
        root.left=insert(root.left,x)
    else:
        root.right=insert(root.right,x)
    return root
def countleaf(root):
    if root==None:
        return 0
    elif root.left==None and root.right==None:
        return 1
    else:
        return countleaf(root.left)+countleaf(root.right)
def print_all_paths(root,p=[]):
    if root==None:
        return 
    p.append(root.data)
    if root.left==None and root.right==None:
        print(p)
        p.pop()
        return
    print_all_paths(root.left,p)
    print_all_paths(root.right,p)
    p.pop()
def level_order_traversal(root,l):
    if root==None:
        return 
    l.append(root)
    while l:
        curr=l.pop(0)
        if curr.left!=None:
            l.append(curr.left)
        if curr.right!=None:
            l.append(curr.right)
        print(curr.data,end=" ")
def count_leafnodes_usinglevelorder(root,l):
    if root==None:
        return
    l.append(root)
    c=0
    while l:
        curr=l.pop(0)
        if curr.left==None and curr.right==None:
            c+=1
        if curr.left!=None:
            l.append(curr.left)
        if curr.right!=None:
            l.append(curr.right)
    print(c)
def left_view(root,c):
    if root==None:
        return
    if c not in d:
        d[c]=root.data
    left_view(root.left,c+1)
    left_view(root.right,c+1)
def right_view(root,c):
    if root==None:
        return
    d[c]=root.data
    right_view(root.left,c+1)
    right_view(root.right,c+1)    
def top_view(root):
    if root==None:
        return
    l=[(root,0)]
    d={}
    while l:
        curr,c=l.pop(0)
        if c not in d:
            d[c]=curr.data
        if curr.left!=None:
            l.append((curr.left,c-1))
        if curr.right!=None:
            l.append((curr.right,c+1))
    for i in sorted(d):
        print(d[i],end=" ")
def bottom_view(root):
    if root==None:
        return
    l=[(root,0)]
    d={}
    while l:
        curr,c=l.pop(0)
        d[c]=curr.data
        if curr.left!=None:
            l.append((curr.left,c-1))
        if curr.right!=None:
            l.append((curr.right,c+1))
    for i in sorted(d):
        print(d[i],end=" ")
#LCA (lowest common ancestor)
# for binary search tree
def lca_bst(root,p,q):
    if root==None:
        return
    if root.data==p or root.data==q:
        return root.data
    if p<root.data and q<root.data:
        return lca_bst(root.left,p,q)
    elif p>root.data and q>root.data:
        return lca_bst(root.right,p,q)
    else:
        return root.data
#for binary tree
def lca_bt(root,p,q):
    if root==None:
        return
    if root.data==p or root.data==q:
        return root.data
    left=lca_bt(root.left,p,q)
    right=lca_bt(root.right,p,q)
    if left!=None and right!=None:
        return root.data
    if left!=None:
        return left
    else:
        return right
def balance_or_not(root):
    if root==None:
        return True
    l=height(root.left)
    r=height(root.right)
    if abs(l-r)>1:
        return False
    return balance_or_not(root.left) and balance_or_not(root.right)
    
root=None
root=insert(root,10)
root=insert(root,5)
root=insert(root,2)
root=insert(root,8)
root=insert(root,7)
root=insert(root,9)
root=insert(root,20)
root=insert(root,15)
root=insert(root,22)
root.inorder(root,)
print()
print(countleaf(root))
print(print_all_paths(root))
level_order_traversal(root,[])
print()
count_leafnodes_usinglevelorder(root,[])
d={}
left_view(root,0)
print("left view",d)
right_view(root,0)
print("right view",d)
top_view(root)
print()
bottom_view(root)
print()
print(lca_bst(root,2,22))
print(lca_bt(root,2,7))
print(balance_or_not(root))