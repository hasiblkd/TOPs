binary_number=int(input("Enter any Binary Number for converting Into Octal:-"))
sum=0
p=0
oct=''

while binary_number!=0:
    rem=binary_number%10
    sum+=(pow(2,p)*rem)
    binary_number=binary_number//10
    p+=1

while sum!=0:
    rem=sum%8
    oct=str(rem)+oct
    sum=sum//8

print("Octal Number:-",oct)