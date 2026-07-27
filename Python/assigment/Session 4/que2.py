mark=int(input("Enter Your Mark::"))
if mark>=101 or mark<=0:
    print("invalid Marks....")
else:
    if mark>=90 and mark<=100:
            print("Grade A...")
    elif mark>75 and mark<89:
            print("Grade B...")
    elif mark>60 and mark<74:
            print("Grade C...")
    elif mark>40 and mark<59:
         print("Grade D...")
    elif mark>0 and mark<40:
            print("Grade F...")