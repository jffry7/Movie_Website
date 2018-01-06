#!/usr/bin/python
# coding=utf-8
import fresh_tomatoes
import media

back_to_future = media.Movie("Back to the Future",
                             "Marty McFly, a 17-year-old high school student, is accidentally sent thirty years into the past in a time-traveling DeLorean invented by his close friend, the maverick scientist Doc Brown.",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BZmU0M2Y1OGUtZjIxNi00ZjBkLTg1MjgtOWIyNThiZWIwYjRiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,643,1000_AL_.jpg",
                             "https://www.youtube.com/watch?v=qvsgGtivCgs")

the_matrix = media.Movie("The Matrix",
                         "A computer hacker Neo learns from mysterious rebels headed by Morpheus about the true nature of his reality and his role in the war against its controllers.",
                         "https://images-na.ssl-images-amazon.com/images/I/51k1epcewKL.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

pirates_caribbean = media.Movie("Pirates of the Caribbean: The Curse of the Black Pearl",
                                "Blacksmith Will Turner teams up with eccentric pirate Captain Jack Sparrow to save his love, the governor's daughter, from Jack's former pirate allies, who are now undead.",
                                "https://image.tmdb.org/t/p/original/aHEDfOxeCWdBhchGwlUQvUOv5Tb.jpg",
                                "https://www.youtube.com/watch?v=0Z1XpfbuZOA")

star_wars = media.Movie("Star Wars: Episode IV - A New Hope",
                        "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empire's world-destroying battle-station while also attempting to rescue Princess Leia from the evil Darth Vader.",
                        "http://movieswithmae.com/wp-content/uploads/2015/05/tvSlBzAdRE29bZe5yYWrJ2ds137.jpg",
                        "https://www.youtube.com/watch?v=vZ734NWnAHA")

star_trek = media.Movie("Star Trek IV: The Voyage Home",
                        "To save Earth from an alien probe, Admiral James T. Kirk and his fugitive crew go back in time to San Francisco in 1986 to retrieve the only beings who can communicate with it: humpback whales.",
                        "https://hustonsite.files.wordpress.com/2016/07/stiv_poster.jpg",
                        "https://www.youtube.com/watch?v=VW7neKZFKE0")

short_circuit = media.Movie("Short Cicuit",
                            "Number 5 (Johnny) of a group of experimental robots in a lab is electrocuted, suddenly becomes intelligent, and escapes.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BZjhlNmI0NDktYTMxNS00MWYwLWEzYjktOTNhN2JkNWFiZTkwXkEyXkFqcGdeQXVyMDEwMjgxNg@@._V1_.jpg",
                            "https://www.youtube.com/watch?v=RBtRVjAMbVo")

movies = [the_matrix, pirates_caribbean, star_wars, star_trek, back_to_future, short_circuit]
fresh_tomatoes.open_movies_page(movies)
