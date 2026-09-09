songs={
    "Winning Speech":4.20,
    "52 Bars":3.50,
    "Tere Liye":3.30
}
def song_duration(song_name):
    try:
        return songs[song_name]
    except KeyError:
        print("Song Duration Not Found")

print(song_duration("Winning Speech"))
print(song_duration("52 Bars2"))
print(song_duration("Tere Liye"))