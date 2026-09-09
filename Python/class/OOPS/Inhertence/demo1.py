class A:

    id=20
    def test(self):
        print("Test Calling.....")

# Inherit Class A

class B(A):
    def sample(self):
        print(self.id)
        print("Sample Calling.....")

b=B()
b.test()
b.sample()