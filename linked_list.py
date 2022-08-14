
class Node: 
    def __init__(self,data) :
        """
          +------+   next or referance or pointer to the next node
          | data |   -----> 
          +------+
        """
        self.data=data
        self.next=None

    def insert_after_x(self,x,newValue):
        """ x is the name of the node befor the new one, not it's data or item 
        the old list :
         | x | --> |x.next|
        the list after inserting :
         |x| --> |new| --> |x.next| 
        """
        # make a new Node object
        new=Node(newValue)
        # Make the referance of the new node points to the referance of the node before it 
        new.next=x.next # |new| --> |x.next|
        # make the referance of x points to the new node
        x.next=new # |x| --> |new| --> |x.next|

    
class LinkedList:
    def __init__(self) :
        self.head=None

    def insert_at_start(self,value):
        """
        the list befor inserting :
         |old_head| --> |old_head.next|
        the list after inserting :
         |new_head| --> |old_head| --> |old_head.next|
        """
        new_head=Node(value)
        old_head=self.head # storing the current head
        new_head.next=old_head # |new_head| --> |old_head|
        self.head=new_head # Updating the old head 
        return self.head 

    def Traversing(self):
        if self.isEmpty()==True:
            print("Empty List :(")
            return # break from the method
        else:
            current=self.head # intial node to start the loop
            while current: # while current is not None
                print(current.data,end="  --> ")
                # break from the loop when you find the last node which points to None
                if current.next == None:
                    print('None')
                    break
                current=current.next # Updating the current node to continue the loop
            
    def isEmpty(self):
        # the list is empty when the the head is None
        if self.head==None:
            isEmpty=True
        elif self.head != None:
            isEmpty=False
        return isEmpty

    def insert_after_data(self,data_befor,newData):
        """befor_data is the data or item to search for and insert new node after it with new data
            |10| --> |30|
            |10(data_befor)| --> |20(newData)| --> |30|
        """
        if self.isEmpty()==True:
            print("List is empty")
            return
        
        new=Node(newData) # new object containing new data to insert
        cur=self.head 
        while cur : # while cur is not None
            # break from the loop if you find the item/data to insert after
            if cur.data == data_befor:
                break
            cur=cur.next 
        if cur == None:
            print("Unfound data in the list :(")
            return
        # if the data is found => cur is should not be None
        elif cur != None:
            new.next=cur.next
            cur.next=new 

    def insert_befor_data(self,dataAfter,newData):
        """
        befor inserting:
            |4|-->|3|
        after inserting:
            |4|-->|6(newData)|-->|3(dataAfter)|
        """
        if self.isEmpty()==True:
            print("List is empty")
            return
        cur=self.head
        nodeToInsert=Node(newData)
        while cur.next:
            if cur.next.data == dataAfter:
                break
            cur=cur.next
        if cur.next == None :
            print("Unfound data")
        else :
            nodeToInsert.next=cur.next 
            cur.next=nodeToInsert  

    def insert_at_position(self,position,newData):
        if position == 1:
            self.insert_at_start(newData)
        i=1
        cur=self.head
        while i < position-1 and cur != None:
            cur=cur.next
            i+=1
        if cur == None :
            print("position out of bound")
        else:
            new=Node(newData)
            new.next=cur.next
            cur.next=new

    def delete_head(self):
        if self.isEmpty()==True:
            print("Empty list")
            return
        else :
            self.head=self.head.next # the new head takes the value of the second node
    
    def delete_tail(self):
        if self.isEmpty()==True:
            print("Empty list")
            return
        else:
            cur=self.head
            #|n|-->|tail|-->None
            while cur.next.next : # to search for the 2nd last node 
                cur=cur.next
            cur.next=None #|n| --> None

    def delete_by_value(self,valueToDelete):
        if self.isEmpty()==True:
            print("Empty list")
            return
        elif valueToDelete==self.head.data:
            self.delete_head()
        else:
            n=self.head
            while n.next != None :
                if n.next.data==valueToDelete:
                    break
                n=n.next
            if n == None:
                print("Unfound value")
                return
            else:
                n.next=n.next.next


    def insert_at_end(self,value): 
        """
        the list befor inserting at the end :
         |last_node|-->None
        the list after inserting :
         |last_node|-->|newTail|-->None
        """
        newTail=Node(value)
        if self.isEmpty()==True:
            self.head=newTail # tail = head in this case
            return # break from the method,All statments bellow will not excute
        cur=self.head # the intial value to start the loop
        while cur.next != None: # Traversing through the list 
            cur=cur.next # update the intial node
        cur.next=newTail # make the last node pointer to the new tail 

# intiate the linked list object
mylist=LinkedList()

#mylist.Traversing()

# make the head of the linked list
head=mylist.insert_at_start(10)
#print(head.data)

# Make the Nodes by calling the Node cls
n1=Node(22)
n2=Node(44)
# Link the Nodes togather
head.next=n1
n1.next=n2

mylist.Traversing()
# inserting 700 befor 44 
mylist.insert_befor_data(44,700)


# inserting after n2
n1.insert_after_x(n2,66)

mylist.Traversing()

# inserting 111 after that node containing 22 
mylist.insert_after_data(22,111)

mylist.insert_at_end(999)

#mylist.delete_tail()
mylist.Traversing()





        