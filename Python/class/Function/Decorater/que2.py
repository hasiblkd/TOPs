# Create Decorator for Calc

def add(or_fun):
    def execute(*a):
        or_fun(*a)
        sum=0
        for i in a:
            sum+=i
        print(sum)
    return execute

def sub(or_fun):
    def execute(*a):
        or_fun(*a)
        sum=0
        for i in a:
            sum-=i
        print(sum)
    return execute

def Mul(or_fun):
    def execute(*a):
        or_fun(*a)
        sum=1
        for i in a:
            sum*=i
        print(sum)
    return execute
@add
@sub
@Mul
def cal(*a):
    print("\tCalc")

cal(10,20,30)