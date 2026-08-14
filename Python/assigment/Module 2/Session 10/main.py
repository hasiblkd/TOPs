# Q2 

# from playlist import add_song,playlist

# print(add_song("Winning Speech",playlist))

# Q-3

# from playlist import add_song,remove_song

# playlist=[]
# print("\t Add Song")
# print(add_song("Keseriya",playlist))
# print(add_song("52 Bars",playlist))
# print(add_song("Winning Speech",playlist))

# print("\t Remove Song")
# print(remove_song("Keseriya",playlist))

# Q-4

from playlist import add_song,remove_song,Display_playlist

playlist=[]
print("\t Add Song")
print(add_song("Keseriya",playlist))
print(add_song("52 Bars",playlist))
print(add_song("Winning Speech",playlist))

print("\t Remove Song")
print(remove_song("Keseriya",playlist))

print("\t Display Song")
print(Display_playlist("",playlist))
