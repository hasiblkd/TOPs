movie_title=['Inception', 'Avatar', 'Joker']
genres=['Sci-Fi', 'Action', 'Drama']
rating=[8.8, 7.8, 8.4]

movie_list=[]

for title,genre,rate in zip(movie_title,genres,rating):
    movie_list.append({
        title:"title",
        genre:"Genres",
        rate:"Rating"
    })

print("Movie Name:-",movie_list)