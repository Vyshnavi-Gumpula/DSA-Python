#check whether given linked list is palindrome r not
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertAtEnd(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=Node(data)
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
    def palindrome(self):
            f=self.head
            s=self.head
            t=self.head
            p=None
            while f!=None and f.next!=None:
                f=f.next.next
                p=s
                s=s.next
            #for even length linked list
            if f==None:
                prev=None
                c=s
                n=None
                while c!=None:
                    n=c.next
                    c.next=prev
                    prev=c
                    c=n
                p.next=prev
                while p.next!=None:
                    if t.data==p.next.data:
                        t=t.next
                        p=p.next
                    else:
                        print("Not palindrome")
                        break
                else:
                    print("palindrome")
            #for odd length linked list
            else:
                prev=None
                c=s.next
                n=None
                while c!=None:
                    n=c.next
                    c.next=prev
                    prev=c
                    c=n
                s.next=prev
                while s.next!=None:
                    if t.data==s.next.data:
                        t=t.next
                        s=s.next
                    else:
                        print("Not palindrome")
                        break
                else:
                    print("palindrome")
                       
l1=LinkedList()
l1.insertAtEnd(10)
l1.insertAtEnd(20)
l1.insertAtEnd(30)
l1.insertAtEnd(30)
l1.insertAtEnd(20)
l1.insertAtEnd(10)
l1.palindrome()
l1.display()
l2=LinkedList()
l2.insertAtEnd(10)
l2.insertAtEnd(20)
l2.insertAtEnd(30)
l2.insertAtEnd(40)
l2.insertAtEnd(30)
l2.insertAtEnd(20)
l2.insertAtEnd(10)
l2.palindrome()
l2.display()