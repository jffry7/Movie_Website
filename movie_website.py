import fresh_tomatoes
import media

back_to_future = media.Movie("Back to the Future",
                             "Marty McFly, a 17-year-old high school student, is accidentally sent thirty years into the past in a time-traveling DeLorean invented by his close friend, the maverick scientist Doc Brown.",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BZmU0M2Y1OGUtZjIxNi00ZjBkLTg1MjgtOWIyNThiZWIwYjRiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,643,1000_AL_.jpg",
                             "https://www.youtube.com/watch?v=qvsgGtivCgs")

movies = [back_to_future]
fresh_tomatoes.open_movies_page(movies)
