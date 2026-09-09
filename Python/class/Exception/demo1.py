# Custom Exception Exmple

class myException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
def chech_age(age):
    if age>18:
        print("Valid....")
    else:
        raise myException("Invalid....")

try:
    chech_age(21)
except myException as e:
    print(e)