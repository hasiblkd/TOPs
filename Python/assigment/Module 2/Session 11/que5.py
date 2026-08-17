import random as r

song_playlist=["Song 1","Song 2","Song 3","Song 4","Song 5","Song 6","Song 7","Song 8"]

today_playlist=r.sample(song_playlist,k=3)

print("Today's Playlist:\n",today_playlist)