class Song:

    def __init__(self,song_name,tittle,duration):
        self.song_name=song_name
        self.tittle=tittle
        self.duration=duration

song_name=input("Enter a song name:-")
song_tittle=input("Enter Song Tittle:-")
song_duration=float(input("Enter a Song Duration:-"))

song_name2=input("Enter a song name:-")
song_tittle2=input("Enter Song Tittle:-")
song_duration2=float(input("Enter a Song Duration:-"))

s1=Song(song_name,song_tittle,song_duration)

s2=Song(song_name2,song_tittle2,song_duration2)

print(s1.song_name)
print(s1.tittle)
print(s1.duration)

print(s2.song_name)
print(s2.tittle)
print(s2.duration)