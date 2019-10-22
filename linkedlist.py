class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def print_node(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next
    def insert(self,data):
        cur_node = Node(data)

        if self.head is None:
            self.head=cur_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=cur_node

    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_after_node(self,pre_node,data):
        if not pre_node:
            print("previous node not in list")
            return
        new_node = Node(data)
        new_node.next=pre_node.next
        pre_node.next=new_node
    def delt_pre(self):
        temp = self.head
        self.head=temp.next
        temp.next=None
        return
    def post_delt(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
        return
    def delt_after_node(self,key):
        temp=self.head
        while temp.data!=key:
            temp=temp.next
        temp.next=temp.next.next
        temp.next.next=None
        return


llist=Linkedlist()


llist.insert("A")
llist.insert("B")
llist.insert("C")

llist.prepend(3)
#llist.delt_pre()
#llist.post_delt()
#llist.delt_after_node("A")
llist.insert_after_node(llist.head.next,7)
llist.print_node()
print(llist.head.data)