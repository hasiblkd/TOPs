class SongAlreadyExistsError(Exception):
    def __init__(self,msg):
            super().__init__(msg)

def Add_Song(playlist,song_name):
    for i in playlist:
        if i==song_name:
            raise SongAlreadyExistsError("Song Already Exist.....")
    playlist.append(song_name)
    print("New Song Add Successfully in Playlist")
    print(playlist)

playlist=['Kesariya', 'Believer', '52 Bars']
        

try:
    song_name=input("Enter a Song name:-")
    Add_Song(playlist,song_name)
except SongAlreadyExistsError as e:
     print(e)