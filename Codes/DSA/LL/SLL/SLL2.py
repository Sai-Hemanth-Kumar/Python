class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

class LinkedList : 
    def __init__(self) :
        self.head = None
    
    def append(self, data) :
        new_node = Node(data)
        if not self.head :
            self.head = new_node
        else :
            temp = self.head
            while temp.next :
                temp = temp.next
            temp.next = new_node

    def remove(self) :
        temp = self.head
        if not temp :
            print("Underflow!")
        elif not temp.next :
            removed_data = temp.data
            self.head = None
            print("Removed", removed_data, "from the Linked List Successfully.")
        else :
            temp = self.head
            prev = None
            while temp.next != None :
                prev = temp
                temp = temp.next
            removed_data = temp.data
            prev.next = None
            print("Removed", removed_data, "from the Linked List Successfully.")

    def display(self) :
        print("Linked List :", end=" ")
        temp = self.head
        while temp :
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def size(self) :
        temp = self.head
        count = 0
        while temp :
            count += 1
            temp = temp.next
        print("Number of elements in the Linked List :", count) 

SLL = LinkedList()
SLL.display()  
SLL.size() 
SLL.remove()
SLL.append(1)
SLL.display()
SLL.append(2)
SLL.display()
SLL.append(3)
SLL.display()
SLL.append(4)
SLL.display()
SLL.append(5)
SLL.display()
SLL.size()
SLL.remove()
SLL.display()
SLL.size()
SLL.remove()
SLL.display()
SLL.size()
SLL.remove()
SLL.display()
SLL.size()
SLL.remove()
SLL.display()
SLL.size()
SLL.remove()
SLL.display()
SLL.size()
SLL.remove()
SLL.display()
SLL.size()


SLL.append(6)
SLL.display()
