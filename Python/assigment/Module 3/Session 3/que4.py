try:
    mylist=[1,2,3]
    print(mylist[5])

except IndexError:
    print("Index Error: List Index Does Not Exist....")

try:
    myDict={'a':1}
    print(myDict['b'])

except KeyError:
    print("Key Error: Dictnory Key Does Not Exist....")