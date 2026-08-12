f=open("test.txt","w")
f.write("Hello, Python")
f.close()

f=open("test.txt","r")
data=f.read()
print(data)