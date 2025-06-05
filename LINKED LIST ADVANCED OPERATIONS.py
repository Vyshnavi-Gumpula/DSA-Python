class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def add_back(self,x):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def display(self):
        t = self.head
        while t!=None:
            print(t.data, end='->')
            t = t.next
        print('None')
    def sum_all(self):
        t=self.head
        s=0
        while(t!=None):
            s=s+t.data
            t=t.next
        print(s)
    def sum_all_even(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
            t=t.next
        print(s)
    def sum_even_pos(self):
        t=self.head
        s=0
        pos=1
        while t!=None:
            if pos%2==0:
                s=s+t.data
            t=t.next
            pos+=1
        print("Sum of elements at even positions:", s)
    def max_ele(self):
        t=self.head
        m=0
        while t!=None:
            if t.data>m:
                m=t.data
            t=t.next
        print(m)
    def second_largest(self):
        t=self.head
        f=0
        s=0
        while t!=None:
            if t.data>f:
                s=f
                f=t.data
            elif t.data>s and t.data!=f:
                s=t.data
            t=t.next
        print(s)
    #find count of contigious pairs with sum<=k
    def contigious_pair(self,k):
        t=self.head
        c=0
        while t.next!=None:
            if t.data+t.next.data<=k:
                c+=1
            t=t.next
        print(c)
    def count_of_pairs(self, k):
        t= self.head
        c = 0
        while t.next!= None:
            t1= t.next
            while t1!= None:
                if t.data+t1.data <= k:
                    c+= 1
                t1=t1.next
            t=t.next
        print("Count of pairs with sum <=", k, "is:", c)
    #given a even linkedlist print the second half of the ll
        #tym complexity o(n)
    def second_half_ofll(self):
        fast=self.head
        slow=self.head
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
        while slow != None:
            print(slow.data, end="->")
            slow = slow.next
        print("None")
    def first_half_ofll(self):
        fast = self.head
        slow = self.head
        t = self.head  
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        while t != slow:
            print(t.data, end="->")
            t = t.next
        print("None")
    #print the kth node from the last
    def kth_node_from_last(self, k):
        fast = self.head
        slow = self.head
        for i in range(k):
            if fast!=None:
                fast = fast.next
        while fast!=None:
            fast = fast.next
            slow = slow.next
        if slow!=None:
            print(slow.data)
    #kth del from last
    def kth_del(self,k):
        fast = self.head
        for i in range(k):
            fast = fast.next
        slow=self.head
        while fast!=None:
            prev=slow
            slow = slow.next
            fast = fast.next
        prev.next=slow.next
    #swap
    def swap(self):
        temp= self.head
        while temp!=None and temp.next!=None:
            temp.data,temp.next.data=temp.next.data,temp.data
            temp=temp.next.next
    #given ll which is unsorted perform bubble sort
    def bubble_sort(self):
        while True:
            f= False
            temp = self.head
            while temp.next !=None:
                if temp.data > temp.next.data:
                    temp.data, temp.next.data = temp.next.data, temp.data
                    f= True
                temp = temp.next
            if f==0:
                break
    def kth_largest_element(self,k):
        temp=self.head
        k1=k
        while temp!=None:
            f=0
            curr=self.head
            while curr.next!=None:
                if curr.data>curr.next.data:
                    f=1
                    curr.data,curr.next.data=curr.next.data,curr.data
                curr=curr.next
            if f==0:
                break
            temp=temp.next
            k-=1
        self.kth_node_from_last(k1)
    #check if there is a loop or not
    def check_loop(self):
        fast = self.head
        slow = self.head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                print("loop is available")
                return
        print("no loop")
    def lengthofll_even_odd(self):
        fast=self.head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
        if fast==None:
            print("even length")
        else:
            print("odd length")
    def starting_point_loop(self):
        fast=self.head
        slow=self.head
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                print("Loop starts at node with data:", slow.data)
                return
        print("No loop found")
    #finding the no of nodes in the loop
    def find_no_of_nodes_loop(self):
        fast=self.head
        slow=self.head
        c=0
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                c= 1
                temp = slow.next
                while temp != slow:
                    c+= 1
                    temp = temp.next
                print("Number of nodes in loop:", c)
                return
        print("No loop found")
    def delete_the_loop(self):
        fast=self.head
        slow=self.head
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = self.head
                while slow != fast:
                    p=fast
                    slow = slow.next
                    fast = fast.next
                p.next=None
                return
        print("No loop found")
    def reverse_ll(self):
        prev=None
        temp=self.head
        while temp!=None:
            next_node=temp.next
            temp.next=prev
            prev=temp
            temp=next_node
        self.head=prev
    def reverse_ll_using_stack(self):
        stack = []
        temp = self.head
        while temp:
            stack.append(temp)
            temp = temp.next
        self.head = stack.pop()
        temp = self.head
        while stack:
            temp.next = stack.pop()
            temp = temp.next
        temp.next = None
        #ll is even length
    def reverse_second_half(self):
        fast=self.head
        slow=self.head
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            prev=slow
            slow = slow.next
        p=None
        c=slow
        while c!=None:
            n=c.next
            c.next=p            
            p=c
            c=n
        prev.next=p
         #ll is odd length
    def rev_sechalf_oddll(self):
        f=self.head
        s=self.head
        while(f!=None and f.next!=None):
            f=f.next.next
            pr=s
            s=s.next
        if f!=None:
            pr=s
            s=s.next
        p=None
        c=s
        while(c!=None):
            n=c.next
            c.next=p
            p=c
            c=n
        pr.next=p

    '''def kth_node_from_last(self,k):
        c=0
        t=self.head
        while t!=None:
            c+=1
            t=t.next
        print(c)
        t=self.head
        for i in range(c-k):
            t = t.next
        print(t.data)'''
    
    '''tym complexity o(2n)
def second_half_ofll(self):
        count = 0
        t = self.head
        while t != None:
            count += 1
            t = t.next
        t = self.head
        for i in range(count//2):
            t = t.next
        while t != None:
            print(t.data, end="->")
            t = t.next
        print("None")'''      
l1=Linkedlist()
l1.head=node(10)
l1.add_back(20)
l1.add_back(33)
l1.add_back(630)
l1.add_back(55)
l1.add_back(600)
l1.display()
l1.sum_all()
l1.sum_all_even()
l1.sum_even_pos()
l1.max_ele()
l1.second_largest()
l1.contigious_pair(30)
l1.count_of_pairs(50)
l1.second_half_ofll()                 
l1.first_half_ofll()                  
l1.kth_node_from_last(2)
l1.display()
l1.kth_del(2)
l1.display()
l1.swap()
l1.display()
l1.bubble_sort()
l1.display()
l1.kth_largest_element(2)
l1.check_loop()
l1.lengthofll_even_odd()
l2=Linkedlist()
l2.head=node(100)
l2.head.next=node(200)
l2.head.next.next=node(300)
l2.head.next.next.next=node(400)
l2.head.next.next.next.next=l2.head.next
l2.check_loop()
l2.starting_point_loop()
l2.find_no_of_nodes_loop()
l2.delete_the_loop()
l2.display()
l2.reverse_ll_using_stack()
l2.display()
l1.display()
l1.reverse_ll()
l1.display()
l2.reverse_second_half()
l2.display()
l1.rev_sechalf_oddll()
