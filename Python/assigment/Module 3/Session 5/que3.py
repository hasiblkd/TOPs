class InstaPost:
    def __init__(self,caption,likes,comment):
        self.caption=caption
        self.likes=likes
        self.comment=comment

    def showPost(self):
        print("Caption:-",self.caption)
        print("Likes:-",self.likes)
        print("Comment:-",self.comment)

    def addComment(self,add_comment):
        self.comment.append(add_comment)
        self.likes+=1

        print("Caption:-",self.caption)
        print("Likes:-",self.likes)
        print("Comment:-",self.comment)

caption=input("Enter a Caption:-")
likes=int(input("Enter a Likes:-"))
comment=input("Enter a Comment's:-")
comment=comment.split(",")

new_comment=input("Enter a new Comment's:-")

in1=InstaPost(caption,likes,comment)

in1.showPost()
in1.addComment(new_comment)