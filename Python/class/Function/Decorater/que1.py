# decorator
def before(or_fun):
    def execute():
        #frist Print Statement then Fuction call
        print("Before Calling.....")
        or_fun()
    return execute

def after(or_fun):
    def execute():
        #frist Fuction call then Print Statement
        or_fun()
        print("After Calling.....")
    return execute

# Decorator Call
@before
@after
def test():
    print("Test Calling....")

test()