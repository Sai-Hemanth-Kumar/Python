num = int(input("Enter a number : "))
for i in range(num) :
    print(" "*(num-1-i), end="")
    print("* ", end="")
    if i != 0 :
        print(" "*(i-1)*2, end="")
        print("*", end="")
    print()
