def read_next_line(lyrics):
    with open(lyrics,"r") as f:
        f.seek(20)
        data=f.readline()
        print(data)
        f.close

read_next_line("lyrics.txt")