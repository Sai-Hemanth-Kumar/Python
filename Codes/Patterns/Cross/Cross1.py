num = int(input("Enter a number : "))
'''for i in range(num) :
    print(" "*i, end="")
    print("*")
print()

for i in range(num):
    print(" "*(num-1-i), end="")
    print("*")
print()'''

'''for i in range(num) :
    print(" "*i, end="")
    print("*", end="")
    print("1"*(num-2-(i*2)), end="")
    print("*")'''

for i in range(num) :
    if i < num//2 :
        print(" "*i,end="")
        print("*", end="")
        print(" "*(num-3-(i*2)),"*")
    elif i == num//2 :
        print(" "*(i-1),"*")
    else :
        count = 0
        print(" "*(num-1-i),end = "")
        print("*", end="")
        print(" " * (num-i), end="")
        print("*")
        count+=1