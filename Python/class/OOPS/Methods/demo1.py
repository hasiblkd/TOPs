class User:
    college="abc"
    def __init__(self,name,email):
        self.name=name
        self.email=email

    def run(self):
        print(self.name,self.email,self.college)

    @classmethod
    def display(cls):
        print(cls.college)

    @staticmethod
    def sample():
        print("Static Method Calling")

User.college="XYZ"

u=User("text","test@gmail.com")
u.run()

u.display()
u.sample()