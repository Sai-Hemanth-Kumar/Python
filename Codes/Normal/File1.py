# Ranged Prime & Composite Numbers

n1 = int(input("Enter number-1 : "))
n2 = int(input("Enter number-2 : "))

if n1 < n2 :
    print("Prime Numbers between", n1, "&", n2, " :", end="")
    for i in range(n1, n2+1) :
        counter = 1
        for j in range(2, i+1) :
            if i%j == 0 :
                counter += counter
        if counter == 2 :
            print(i, end=" ")

else :
    print("Invalid range!")     