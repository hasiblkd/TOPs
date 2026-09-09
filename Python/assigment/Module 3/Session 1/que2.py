f=open("my_fav_song.txt","r")
data=f.readlines()

count=1

for i in data:
    print(count,".",i)
    count+=1

