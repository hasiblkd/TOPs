print("Armstrong Number's are between 0-999...\n")
for num in range(1,1000):
    temp=num
    sum=0
    while num!=0:
        rem=num%10
        sum+=pow(rem,3)
        num=num//10

    if sum==temp:
        print(sum)
    else:
        pass