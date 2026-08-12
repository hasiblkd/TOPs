num=int(input("Enter a No. Row's:-"))
i=1
while i<=num:
    space=1
    while space<=num-i:
        print(" ",end="")
        space+=1
    star=1
    while star<=(2*i-1):
        print("*",end="")
        star+=1
    print()
    i+=1