# Reverse Diamond Pattern
num = int(input("Enter a number : "))
print("Reverse Right Triangle")
for i in range(1,num+1) :
    print("  " * (num-i), end="")
    for j in range (i,0,-1) :
        print(j, end=" ")
    print()

print("\nReverse Left Triangle")
for i in range (1, num+1) :
    for j in range (1, i+1) :
        print(j, end=" ")
    print()
    
print("\nInverse Reverse Right Triangle")
for i in range (num, 0, -1) :
    print("  " * (num-i), end="")
    for j in range (i, 0, -1) :
        print(j, end=" ")
    print()

print("\nInverse Reverse Left Triangle")
for i in range (num, 0, -1) :
    for j in range (1, i+1) :
        print(j, end=" ")
    print()
    
print("\nReverse Diamond")
for i in range(1,num+1) :
    print("  " * (num-i), end="")
    for j in range (i,0,-1) :
        print(j, end=" ")
    for j in range (2, i+1) :
        print(j, end=" ")
    print()
for i in range (num-1, 0, -1) :
    print("  " * (num-i), end="")
    for j in range (i, 0, -1) :
        print(j, end=" ")
    for j in range (2, i+1) :
        print(j, end=" ")
    print()