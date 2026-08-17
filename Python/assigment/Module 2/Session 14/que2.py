def add_song_to_playlist(playlists, user, playlist_name, song_title, artist):
    if user not in playlists:
        playlists[user]={}

    if playlist_name not in user:
        playlists[user][playlist_name]=[]

    playlists[user][playlist_name].append({
        "Title":song_title,
        "Artist":artist
    })

    return playlists

playlists={}

add_song_to_playlist(
    playlists,
    "Hasib",
    "My Favorite",
    "Winning Speech",
    "Karan Aujla"
)

print(playlists)














#     playlists={user:{
#         playlist_name:{
#             "Tittle":song_title,"Artist Name":artist
#         }
#     }}
    
#     print(playlists)
    
# add_song_to_playlist(playlists="Spotify",user="Hasib",playlist_name="My Favorite",song_title="Winning Speech",artist="Karan Aujla")