#mark=int(input("Enter Your Mark::"))
flag='y'
while flag=='y':
    mark=int(input("Enter Your Mark::"))
    if mark>=101 or mark<=0:
        print("invalid Marks....")
    else:
        if mark>=91 and mark<=100:
            print("Grade A...")
        elif mark>71 and mark<90:
            print("Grade B...")
        elif mark>51 and mark<70:
            print("Grade C...")
        elif mark>35 and mark<50:
         print("Grade D...")
        elif mark>0 and mark<34:
            print("Your Fail...")
    
    flag=input("if you want to continue then press 'y' and not so press 'n':")
    if flag=='n':
        print("Your are Exit...")