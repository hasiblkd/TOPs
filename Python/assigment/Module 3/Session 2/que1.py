f=open("lyrics.txt","w")
f.write("Hello, My name is Hasib...")
f.close()

f=open("lyrics.txt","r")
data=f.read(10)
print(data)
print(f.tell())
f.close()
