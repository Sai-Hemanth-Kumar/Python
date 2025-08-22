class Stack :
    def __init__(self) :
        self.stack = []
    
    def push(self, data) :
        self.stack.append(data)
        print("Pushed", data, "into Stack Successfully.")
    
    def pop(self) :
        temp = self.stack.pop()
        print("Underflow!") if not temp else print("Popped", temp, "from Stack Successfully.")

    def TopOfStack(self) :
        print("Top of Stack : Underflow") if not self.stack else print("Top of Stack :", self.stack[-1]) 

    def display(self) :
        print("Stack : ", end="")
        if not self.stack :
            print("Underflow", end=" ") 
        for i in self.stack :
            print(i, end=" ")
        print()
    
    def size(self) :
        print("Number of elements in the Stack :", len(self.stack))

stk = Stack()
stk.display()
stk.push(1)
stk.display()
stk.push(2)
stk.display()
stk.push(3)
stk.display()
stk.push(4)
stk.display()
stk.push(5)
stk.display()
stk.push(6)
stk.display()
stk.push(7)
stk.display()
stk.size()
stk.pop()
stk.display()
stk.pop()
stk.display()
stk.TopOfStack()
stk.size()