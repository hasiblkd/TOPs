class Content():
    def Display(self,title):
        print("Title:-",title)

class Movie(Content):
    def Display(self, title,year):
        print("Title:-",title)
        print("Year:-",year)

title=input("Enter a Title:-")
year=input("Enter a Year:-")

c1=Content()
m1=Movie()

c1.Display(title)
m1.Display(title,year)