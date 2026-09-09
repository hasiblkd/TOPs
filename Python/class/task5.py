# num=int(input("Enter a number:-"))
# for i in range(num):
#     for j in range(i+1):
#         print("*",end="")
#     print()


k=["java","Python","Php","Android"]
ans=[i for i in k if i.startswith("P")]
print(list(ans))
