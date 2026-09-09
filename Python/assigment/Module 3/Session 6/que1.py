class User:

    def __init__(self,username,email):
        self.username=username
        self.email=email

    def showUser(self):
        print("Username:-",self.username)
        print("Email:-",self.email)

username=input("Enter Username:-")
email=input("Enter Email:-")

u1=User(username,email)
u1.showUser()