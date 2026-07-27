# Money Double Program
money=1
add=0
#mul=2
for i in range(1,31):
    money*=2
    print("day's:-",i)
    print("Money:-",money)
    add+=money

print("Sum of Moeny is ",add)