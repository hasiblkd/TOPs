# Q1
def add_song(song_name, playlist):
    playlist.append(song_name)
    return playlist

# playlist=[]
# print(add_song("Keseriya",playlist))
# print(add_song("52 Bars",playlist))

#Q-3
def remove_song(song_name, playlist):
    if song_name in playlist:
        playlist.remove(song_name)
    return playlist

# Q-4

def Display_playlist(song_name, playlist):
    for i in playlist:
        print(i,".",song_name)
    return playlist