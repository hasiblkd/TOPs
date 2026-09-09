with open("playlist.txt","w") as f:
    f.write("Winning Speech\n")
    f.write("Boom Saka\n")
    f.write("52 Bars\n")
    f.write("Keseriya\n")
    f.write("Tere Liye")
    f.close()

with open("playlist.txt","r") as f:
    f.seek(25)
    data=f.readline()
    print(data.strip())
    f.close()