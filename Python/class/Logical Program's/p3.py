#fibonacie series using for..loop
#num=int(input("Enter Number for Fibo-Series::"))
#a=0
#b=1
#for i in range(num):
#    print(a,end=" ")
#    c=a+b
#    a=b
#    b=c

#fibonacie series using while..loop

num=int(input("Enter Number for fibo-Series::"))
a=0
b=1
count=0

while count<num:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    count+=1