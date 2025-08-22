# '+' Pattern using '*'
try :
    while (True) :
        num = int(input("Enter an odd number greater than 1 : "))
        if not type(num) is int:
            raise TypeError("Only integers are allowed!")
        if num <= 1 :
            print("Invalid Input to create pattern!")
        elif num%2 == 0 :
            print("Even number can not visually create a great pattern!")
        else :
            for i in range(num) :
                if i == num//2 :
                    for j in range(num) :
                        print("*", end=" ")
                else :
                    print(" " * (num-1), end="")
                    print("*",end="")
                print()
        flag = input("Want to continue? yes/no : ")
        if not flag.isalpha() :
            raise TypeError("Invalid DataType at flag!")
        if flag.lower() != 'yes' :
            break
            
except Exception as e:
    print("Error :", e)
finally :
    print("Finally Block Executed Successfully after Try-Except")