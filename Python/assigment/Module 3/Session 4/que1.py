class InvaliedCuponCodeError(Exception):
    def __init__(self,msg):
        super().__init__(msg)

def CheckCupon(ch_cupon):
    
    cupon_list=["save10","save20","food50"]
    for cupon in cupon_list:
        if cupon==ch_cupon:
            print("Valid Cupon...")
            break
        else:
            raise InvaliedCuponCodeError("Invalid Cupon.....")

try:
    print("======== Available Cupon =======")
    print("1. save10")
    print("2. save20")
    print("3. food50")
    cupon=input("Enter Cupon:-")

    CheckCupon(cupon)
except InvaliedCuponCodeError as e:
    print(e)