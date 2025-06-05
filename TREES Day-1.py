class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def inOrder(self,root):
        if root==None:
            return
        self.inOrder(root.left)
        print(root.data,end=" ")
        self.inOrder(root.right)
    def preOrder(self,root):
        if root==None:
            return
        print(root.data,end=" ")
        self.inOrder(root.left)
        self.inOrder(root.right)
    def postOrder(self,root):
        if root==None:
            return
        self.inOrder(root.left)
        self.inOrder(root.right)
        print(root.data,end=" ")
    def sum_all_nodes(self,root):
        if root==None:
            return 0
        return root.data+self.sum_all_nodes(root.left)+self.sum_all_nodes(root.right)
    def sum_of_even(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return root.data+self.sum_of_even(root.left)+self.sum_of_even(root.right)
        else:
            return self.sum_of_even(root.left)+self.sum_of_even(root.right)
    def height(self,root):
        if root==None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
    def search(self,root,s):
        if root==None:
            return False
        if root.data==s:
            return True
        elif root.data>s:
            return self.search(root.left,s)
        return self.search(root.right,s)
    def insert(self,root,data):
        if root==None:
            return node(data)
        if data<root.data:
            root.left=self.insert(root.left,data)
        else:
            root.right=self.insert(root.right,data)
        return root
    def count_leaf_nodes(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        return self.count_leaf_nodes(root.left)+self.count_leaf_nodes(root.right)
root=node(10)
root.left=node(5)
root.right=node(20)
root.left.left=node(2)
root.left.right=node(8)
root.inOrder(root)
print()
root.preOrder(root)
print()
root.postOrder(root)
print()
print(root.sum_all_nodes(root))
print(root.sum_of_even(root))
print(root.height(root))
print(root.search(root,11))
root=node(10)
root.insert(root,5)
root.insert(root,20)
root.insert(root,2)
root.insert(root,12)
root.insert(root,23)
root.inOrder(root)
print()
print(root.count_leaf_nodes(root))

