num=int(input("Enter a number:-"))
for i in range(num):
    for j in range(num):
        if j==0 or j==4 or i==num-3:
            print("* ",end="")
        else:
            print("  ",end="")
    print()