def right_triangle(n):
    for i in range(n+1):
        for j in range(i):
            print("*",end="")
        print("\n")

n=int(input("enter number : "))
right_triangle(n)