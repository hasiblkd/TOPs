f=open("my_fav_song.txt","a")
f.writelines("Hangour\n")
f.writelines("Sanam Teri Kasam")
f.close()

f=open("my_fav_song.txt","r")
data=f.readlines()
count=1

for i in data:
    print(count,".",i)
    count+=1