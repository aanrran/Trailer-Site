import Movie
import fresh_tomatoes

#create movies that goes into the trailer webpage
rogue_one = Movie.Movie("Rogue One", "Rogue One",
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",
                        "https://youtu.be/frdj1zb9sMY")
life_of_pi = Movie.Movie("Life of Pi",
                         "In Life of Pi, Yann Martel uses faith to determine "
                         "which story of Pi's survival on the lifeboat to believe.",
                         "https://upload.wikimedia.org/wikipedia/en/5/57/Life_of_Pi_2012_Poster.jpg",
                         "https://youtu.be/j9Hjrs6WQ8M")
birth_of_the_drangon = Movie.Movie("Birth Of The Drangon",
                                   "The true story revolves around the young martial artist Bruce Lee, "
                                   "who challenges kung fu master Wong Jack Man in 1965 in San Francisco.",
                                   "https://upload.wikimedia.org/wikipedia/en/d/d0/Birth_of_the_Dragon_poster.jpg",
                                   "https://youtu.be/vbNib_NsVRU")

#store all the movie object created onto a list
movies = [rogue_one, life_of_pi, birth_of_the_drangon]

#generate the webpage
fresh_tomatoes.open_movies_page(movies)
