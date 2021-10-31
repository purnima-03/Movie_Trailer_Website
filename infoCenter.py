import fruitM
import movie_trailer

apple=media.Movie("Apple", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUbH4B5xoe9r6SUvIIYMQIYGDWDDtisssKiQuIa0oJYlI_Y9x5")
#print (toy_story.storyline)

mango=media.Movie("Mango",)

#avatar.show_trailer()

banana=media.Movie("Banana",
                    "A group of mammals surviving the Paleolithic ice age",
                    "https://fanart.tv/fanart/movies/950/movieposter/ice-age---the-meltdown-52a89da5da857.jpg",
                    "https://www.youtube.com/watch?v=cMfeWyVBidk")
#print(ice_age.storyline)
#ice_age.show_trailer()

orange=media.Movie("Orange",
                  "In the near future, a weary Logan (Hugh Jackman) cares for an ailing Professor X (Patrick Stewart) at a remote outpost on the Mexican border. His plan to hide from the outside world gets upended when he meets a young mutant (Dafne Keen) who is very much like him. Logan must now protect the girl and battle the dark forces that want to capture her.",
                  "http://logan-touch.foxfilm.com/backgrounds_logan_outer.jpg",
                  "https://www.youtube.com/watch?v=RH3OxVFvTeg")

strawberry=media.Movie("Strawberry",
                       "Four animals from the New York Central Zoo, with a spoiled upbringing, escape, unintentionally helped by four fugitive penguins. They find themselves in Madagascar subsequently amidst happy lemurs.",
                       "http://static.rogerebert.com/uploads/movie/movie_poster/madagascar-2005/large_yumzX3Fn7geEKEjuAGNcRjZETPE.jpg",
                       "https://www.youtube.com/watch?v=fq5zU9T_Hl4")

pomegrante=media.Movie("Pomegrante",
                             "A computer whiz, a hot-shot pilot, the U.S. President and a group of ragtag survivors unite to save mankind after an alien race invades Earth and destroys all its major cities.",
                             "https://i.ytimg.com/vi/FvzqC8j8Tj8/maxresdefault.jpg",
                             "https://www.youtube.com/watch?v=B1E7h3SeMDk")

pear=media.Movie("Pear",
                      "Tris, an adult resident of a futuristic world divided into five factions, elects to join the Dauntless faction. But she actually belongs to another faction, which she must hide, as a major war looms.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYxMzYwODE4OV5BMl5BanBnXkFtZTgwNDE5MzE2MDE@._V1_UY1200_CR69,0,630,1200_AL_.jpg"
                      "https://www.youtube.com/watch?v=sutgWjz10sM")

grape=media.Movie("Grape",
                 "Scientists, soldiers and adventurers unite to explore a mythical, uncharted island in the Pacific Ocean. Cut off from everything they know, they venture into the domain of the mighty Kong, igniting the ultimate battle between man and nature. As their mission of discovery soon becomes one of survival, they must fight to escape from a primal world where humanity does not belong.",
                 "http://coolandcollected.com/wp-content/uploads/2017/02/kong-skull-island-poster-king.jpg",
                 "https://www.youtube.com/watch?v=44LdLqgOpjo")


movies=[apple, mango, banana, orange, strawberry, pomegrante, pear, grape]
#fresh_tomatoes.open_movies_page(movies)                             

#print(media.Movie.VALID_RATINGS)

print(fruitM.Movie.__doc__)
