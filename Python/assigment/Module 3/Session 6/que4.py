class User:

    def __init__(self,username,email):
        self.username=username
        self.email=email

class Influencer(User):

    def showUser(self,followers):

        self.followers=followers

class Brand:
    def __init__(self,brandname):
        self.brandname=brandname

class BrandPartner(Influencer,Brand):
    def __init__(self, username, email,follower,brandname):
        User.__init__(self,username, email)
        self.followers=follower
        Brand.__init__(self,brandname)

    def showBrandPartner(self):
        print("Username:-",self.username)
        print("Email:-",self.email)
        print("Follwers:-",self.followers)
        print("Brand Name:-",self.brandname)



username=input("Enter Username:-")
email=input("Enter Email:-")
followers=int(input("Enter Followers:-"))
b_name=input("Enter a Brand Name:-")

b1=BrandPartner(username,email,followers,b_name)
b1.showBrandPartner()