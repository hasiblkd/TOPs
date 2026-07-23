number=49
gusse_number=int(input("Enter Your Gussing number:-"))
if gusse_number<0:
    print("Nagetive Number not Allowed...")
else:
    if gusse_number>number:
        print("Too High...")
    elif gusse_number<number:
        print("Too Low...")
    else:
        print("Congratulation. You Guess the Number...")