f=open("test2.txt","w")
l=["Hello, Python \n","Hello, Java \n","Hello, PHP \n","Hello, Android \n","Hello, JavaScript \n"]
f.writelines(l)
f.close()


f=open("test.txt","r")
data=f.read()
len=0
