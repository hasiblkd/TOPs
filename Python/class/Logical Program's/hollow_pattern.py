print("======================================")
print("       HOLLOW PATTERN MENU")
print("======================================")
print("1.  Hollow Square                    ✅")
print("2.  Hollow Rectangle                 ✅")
print("3.  Left C Pattern                   ✅")
print("4.  Right C Pattern                  ✅")
print("5.  U Pattern                        ✅")
print("6.  L Pattern                        ✅")
print("7.  Hollow Left Triangle             ✅")
print("8.  Hollow Right Triangle            ✅")
print("9.  Hollow Triangle                  ✅")
print("10. Hollow Inverted Left Triangle    ✅")
print("11. Hollow Inverted Right Triangle   ✅")
print("12. Hollow Inverted Triangle         ✅")
print("13. Hollow Pyramid                   ✅")
print("14. Hollow Hourglass                 ✅")
print("15. Hollow Inward Hourglass          ✅")
print("16. Butterfly Pattern                ✅")
print("17. Hollow Diamond                   ✅")
print("18. Hollow X Pattern                 ✅")
print("19. Hollow Plus (+)                  ⏳")
print("20. Hollow Rhombus                   ⏳")
print("21. Hollow Parallelogram             ⏳")
print("22. Hollow Arrow                     ⏳")
print("23. Hollow Kite                      ⏳")
print("24. Hollow Circle                    ⏳")
print("25. Exit")
print("======================================")

ch=int(input("Enter Your Choice: "))
num=int(input("Enter a No of Row's:-"))

match(ch):
    case 1:
        for i in range(num):
            for j in range(num):
                if j==0 or j==num-1 or i==0 or i==num-1:
                    print("* ",end="")
                else:
                    print("  ",end="")
            print()
    case 2:
        for i in range(num):
            for j in range(num+2):
                if j==0 or j==num+1 or i==0 or i==num-1:
                    print("* ",end="")
                else:
                        print("  ",end="")
            print()
    case 3:
        for i in range(num):
            for j in range(num):
                if j==0 or i==num-1 or i==0:
                    print("* ",end="")
                else:
                    print(" ",end="")
            print()
    case 4:
        for i in range(num):
            for j in range(num):
                if i==num-1 or i==0 or j==num-1:
                    print("* ",end="")
                else:
                    print("  ",end="")
            print()
    case 5:
        for i in range(num):
            for j in range(num):
                if i==num-1 or j==0 or j==num-1:
                    print("* ",end="")
                else:
                    print("  ",end="")
            print()
    case 6:
        for i in range(num):
            for j in range(num):
                if i==num-1 or j==0:
                    print("* ",end="")
                else:
                    print("  ",end="")
            print()
    case 7:
        for i in range(num):
            for j in range(i+1):
                if j==0 or i==num-1 or j==i:
                    print("* ",end="")
                else:
                    print("  ",end="")
            print()
    case 8:
        for i in range(num):
            for k in range((num-1)-i):
                print(" ",end="")
            for j in range(i+1):
                if j==0 or i==j or i==num-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
    case 9:
        for i in range(num):
            for k in range(num-i):
                print(".",end="")
            for j in range((i*1)+1):
                if j==0 or j==i or i==num-1:
                    print("* ",end="")
                else:
                    print("  ",end="")
            print()
    case 10:
        for i in range(num):
            for j in range(num-i):
                if j==0 or i==0 or j==num-(i+1):
                    print("* ",end="")
                else:
                    print("  ",end="")
            for k in range(i+1):
                print("  ",end="")
            print()
    case 11:
        for i in range(num):
            for j in range(i+1):
                print(" ",end="")
            for k in range(num-i):
                if i==0 or k==0 or k==num-i-1 :
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
        print()
    case 12:
        for i in range(num):
            for j in range(i+1):
                print(" ",end="")
            for k in range(num-i):
                if k==0 or i==0 or k==num-i-1:
                    print("* ",end="")
                else:
                    print("  ",end="")
            print()
    case 13:
        for i in range(num):
            for j in range(num-i):
                print(" ",end="")
            for k in range((i*2)+1):
                if k==0 or i==num-1 or k==i*2:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
    case 14:
        for i in range(num-1):
            for j in range(num-i):
                print(" ",end="")
            for k in range(i+1):
                if k==0 or k==i:
                    print("* ",end="")
                else:
                    print("  ",end="")
            print()
        for i in range(num):
            for j in range(i+1):
                print(" ",end="")
            for k in range(num-i):
                if k==0 or k==num-(i+1):
                    print("* ",end="")
                else:
                    print("  ",end="")
            print()
    case 15:
        for i in range(num-1):
            for j in range(i+1):
                print(" ",end="")
            for k in range(num-i):
                if k==0 or i==0 or k==num-(i+1):
                    print("* ",end="")
                else:
                    print("  ",end="")
            print()

        for i in range(num):
            for j in range(num-i):
                print(" ",end="")
            for k in range(i+1):
                if k==0 or k==i or i==num-1:
                    print("* ",end="")
                else:
                    print("  ",end="")
            print()
    case 16:
        for i in range(num):
            for j in range(i+1):
                if j==0 or i==j:
                    print("*",end="")
                else:
                    print(" ",end="")
            for k in range(2*(num-i-1)):
                print(" ",end="")

            for j in range(i+1):
                print("*",end="")
            print()

        for i in range(num-2,-1,-1):
            for j in range(i+1):
                print("*",end="")
            for k in range(2*(num-i-1)):
                print(" ",end="")
            for j in range(i+1):
                print("*",end="")
            print()
    case 17:
        for i in range(num):
            for j in range(num-i):
                print(" ",end="")
            for k in range((i*2)+1):
                if k==0 or k==i*2:
                    print("*",end="")
                else:
                    print(".",end="")
            print()

        for i in range(num,-1,-1):
            for j in range(num-i):
                print(" ",end="")
            for k in range((i*2)+1):
                if k==0 or k==2*i:
                    print("*",end="")
                else:
                    print(".",end="")
            print()
    case 18:
        for i in range(num-1,0,-1):
            for j in range(num-i):
                print(" ",end="")
            for k in range((i*2)+1):
                if k==0 or k==i*2:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()

        for i in range(num):
            for j in range(num-i):
                print(" ",end="")
            for k in range((i*2)+1):
                if k==0 or k==i*2:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
    case _:
        print("Invalid Choice.....")
        