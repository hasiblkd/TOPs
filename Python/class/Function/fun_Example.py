# define Function
def hello():
    print("Hello World.....")

# Calling Function

hello()

# Example 1

def Squre(a):
    print(a*a)

Squre(5)





# Example of Using Return Keyword

def Mess():
    return "Hello, Hasib..."

# Method 1
mess=Mess()
print(mess)

# Method 2

print(Mess())

# Example 2

def Cube(a):
    return pow(a,3)

print(Cube(3))

# * is create Tuple and Its called Arbeteri Argument
# ** is Create Dictnory for Store data in a Key ans Value.

def sum(*c):
    sum=0
    for i in sum:
        sum+=i
    print(sum)

def person(**data):
    print(data)

person(name="Hasib")


def student(name="Hasib",email="hasiblkd@gmail.com",age=0):
    print(name,email,age=23)

student(email="abc@gmail.com")

# Lambda Function

sum=lambda a,b: a+b
print(sum(10,20))

msg= lambda : "Hello, Hasib..."
print(msg())