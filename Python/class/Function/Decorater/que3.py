def only_number(or_fun):
    def num(data):
        if str(data).isdigit():
            or_fun(data)
        else:
            print("Only Number Allowed...")
    return num

def only_txt(or_fun):
    def taxt(data):
        if str(data).isalpha():
            or_fun(data)
        else:
            print("Only Text Allowed...")
    return taxt


# @only_number
@only_txt
def getdata(data):
    print("data is",data)

getdata("ghvj")
