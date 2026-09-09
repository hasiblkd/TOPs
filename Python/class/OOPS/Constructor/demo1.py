class Student:

    def __init__(self,id,name,email):
        self.id=id
        self.name=name
        self.email=email

    def disply_student(self):
        print(self.id,self.name,self.email)

# Without User Inpur
# s=Student(10,"Hasib","hasib@gmail.com")

# With User Inpur
id=input("Enter Id:-")
name=input("Enter Name:-")
email=input("Enter Email:-")

ans=Student(id,name,email)
ans.disply_student()
