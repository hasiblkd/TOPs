num=int(input("Enter a Number:"))
for i in range(num+1):
    for j in range(num-i,num):
        print(j+1,end="")
    print()    