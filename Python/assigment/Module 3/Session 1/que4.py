f=open("my_fav_song.txt","r")
data=f.readlines()
count=0
for i in range(len(data)):
    count+=1

print("Total Song:-",count)