class User:

    def __init__(self,username,email):
        self.username=username
        self.email=email

class Influencer(User):

    def showUser(self,followers):

        self.followers=followers

        print("Username:-",self.username)
        print("Email:-",self.email)
        print("Follwers:-",self.followers)

username=input("Enter Username:-")
email=input("Enter Email:-")
followers=int(input("Enter Followers:-"))

i1=Influencer(username,email)
i1.showUser(followers)