class User:

    def __init__(self,username,email):
        self.username=username
        self.email=email

class Influencer(User):

    def showUser(self,followers):

        self.followers=followers

class VerifyedInfluencer(Influencer):

    def showVerifiedInfluencer(self,badge):

        self.badge=badge

        print("Username:-",self.username)
        print("Email:-",self.email)
        print("Follwers:-",FormatingFollower(self.followers))
        print("Badge",self.badge)

def FormatingFollower(followers):
    if followers>=10000000:
        return str(followers/10000000)+"M"
    elif followers>1000:
        return str(followers/1000)+"K"
    else:
        return str(followers)
username=input("Enter Username:-")
email=input("Enter Email:-")
followers=int(input("Enter Followers:-"))
badge=input("Enter a Badge:-")
vi1=VerifyedInfluencer(username,email)
vi1.showUser(followers)
vi1.showVerifiedInfluencer(badge)