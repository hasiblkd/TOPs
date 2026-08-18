print("==============================================")
print("        🔢 NUMBER PATTERN PRACTICE")
print("==============================================")
print("\tBASIC PATTERNS")
print("1.  Increasing Numbers                ✅")
print("2.  Repeated Number                   ✅")
print("3.  Same Number in Each Row           ⏳")
print("4.  Decreasing Numbers                ⏳")
print("5.  Reverse Numbers                   ⏳")
print("6.  Row Number Starting From 1        ⏳")

print("\tINTERMEDIATE PATTERNS")
print("7.  Continuous Number Triangle        ⏳")
print("8.  Reverse Number Triangle           ⏳")
print("9.  Repeated Row Number               ⏳")
print("10. Reverse Repeated Number           ⏳")
print("11. Right-Aligned Number Triangle     ⏳")
print("12. Right-Aligned Repeated Numbers    ⏳")

print("\tADVANCED PATTERNS")
print("13. Number Pyramid                    ⏳")
print("14. Repeated Number Pyramid           ⏳")
print("15. Continuous Number Pyramid         ⏳")
print("16. Reverse Pyramid                   ⏳")
print("17. Number Diamond                    ⏳")
print("18. Repeated Number Diamond           ⏳")

print("\tEXPERT PATTERNS")
print("19. Floyd's Triangle                  ⏳")
print("20. Reverse Floyd's Triangle          ⏳")
print("21. 0-1 Triangle                      ⏳")
print("22. Alternating Number Triangle       ⏳")
print("23. Alternating 1-0 Rows              ⏳")
print("24. Pascal's Triangle                 ⏳")

print("\tCHALLENGE PATTERNS")
print("25. Number X Pattern                  ⏳")
print("26. Number Butterfly                  ⏳")
print("27. Hollow Number Square              ⏳")
print("28. Hollow Number Pyramid             ⏳")
print("29. Number Spiral                     ⏳")
print("30. Continuous Number Diamond         ⏳")

print("==============================================")
print("0.  Exit")
print("==============================================")

choice = int(input("Enter your choice: "))
num=int(input("Enter No. of Row's:-"))
match choice:
    

    case 1:
        print("Increasing Numbers")
        for i in range(num):
            for j in range(i+1):
                print(j+1,end="")
            print()

    case 2:
        print("Repeated Number")
        for i in range(num):
            for j in range(i+1):
                print(i+1,end="")
            print()

    case 3:
        print("Same Number in Each Row")
        for i in range(num):
            for j in range(num):
                print(i+1,end="")
            print()

    case 4:
        print("Decreasing Numbers")
        for i in range(num):
            for j in range(num-i):
                print(j+1,end="")
            print()

    case 5:
        print("Reverse Numbers")
        for i in range(num):
            for j in range(num,i,-1):
                print(j,end="")
            print()

    case 6:
        print("Row Number Starting From 1")
        for i in range(num):
            for j in range(i+1):
                print(j+1,end="")
                j+=1
            print()

    case 7:
        print("Continuous Number Triangle")

    case 8:
        print("Reverse Number Triangle")

    case 9:
        print("Repeated Row Number")

    case 10:
        print("Reverse Repeated Number")

    case 11:
        print("Right-Aligned Number Triangle")

    case 12:
        print("Right-Aligned Repeated Numbers")

    case 13:
        print("Number Pyramid")

    case 14:
        print("Repeated Number Pyramid")

    case 15:
        print("Continuous Number Pyramid")

    case 16:
        print("Reverse Pyramid")

    case 17:
        print("Number Diamond")

    case 18:
        print("Repeated Number Diamond")

    case 19:
        print("Floyd's Triangle")

    case 20:
        print("Reverse Floyd's Triangle")

    case 21:
        print("0-1 Triangle")

    case 22:
        print("Alternating Number Triangle")

    case 23:
        print("Alternating 1-0 Rows")

    case 24:
        print("Pascal's Triangle")

    case 25:
        print("Number X Pattern")

    case 26:
        print("Number Butterfly")

    case 27:
        print("Hollow Number Square")

    case 28:
        print("Hollow Number Pyramid")

    case 29:
        print("Number Spiral")

    case 30:
        print("Continuous Number Diamond")

    case 0:
        print("Thank You!")

    case _:
        print("Invalid Choice!")