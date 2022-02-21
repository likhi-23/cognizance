n = int(input("Enter the number of rows:"))
for p in range (n) :
    for q in range(n-p-1) :
        print(" ",end="")
    for q in range(p+1):
        print("*",end=" ")
    print()
