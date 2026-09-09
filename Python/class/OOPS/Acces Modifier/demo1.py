class demo:

    #public
    name="Hasib"

    #Protected
    _email="hasiblkd123@gmail.com"

    # Private
    __age=23

    def test(self):
        print(self.name,self._email,self.__age)

d=demo()
# Public Access Specifier Call,Value Change
d.name="abc"
# Protected Access Specifier Call,Value Change
d._email="abc@gmail.com"
# Private Access Specifier Call,Value Change
d.__age=30
# in Python, we cant change value of private memeber becuse python by default change a name. it's add _classname.
d._demo__age=31

d.test()