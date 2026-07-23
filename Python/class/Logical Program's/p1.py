#for i in range(0,101):
#    if i%2==0:
#        print(i," is Even Number")
#    else:
#        print(i," is Odd Number")
#num=int(input("Enter a range that you want to print Prime number::"))
num=101
flag=0
for i in range(2,num):
    if num%i==0:
        flag=1
        break

if flag==0:
    print("Prime Number")
else:
    print("not Prime Number")