class Node():

    def __init__(self, data):

        self.data = data
        self.ref = None

class linkedList():

    def __init__(self):

        self.head=None



    
    def print_LL(self):

        if self.head == None:

            print("Linked List is Empty")
            
    
        else:

            n = self.head

            while n is not None:
                print(n.data)
                n = n.ref


    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):

        new_node= Node(data)

        if self.head is None: #if head is Empty

            self.head=new_node #Assign node to the head
        else:

            n = self.head 

            while n.ref is not None: #loop until n.ref (each node) until last node points towards None/Null.

                n=n.ref

            n.ref= new_node #pointing the ref to the last node ( which was pointing to null earlier)
LL1= linkedList()

LL1.add_begin(10)

LL1.add_end(100)

LL1.add_begin(20)

LL1.print_LL()
