#!/usr/bin/env python
import media
#import ud036_StarterCode.fresh_tomatoes as ft #  import fresh tomatoes
from ud036_StarterCode.fresh_tomatoes import open_movies_page # from fresh_tomatoes module, import open_moviespage function

toystory = media.Movie("Toy Story","story of a boy and his toys that comes to life",
                       "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc","81")

terminator = media.Movie("The Terminator", "A seemingly indestructible humanoid cyborg is sent from 2029 to 1984",
                         "https://vignette1.wikia.nocookie.net/terminator/images/c/ca/Terminator_poster.jpg/revision/latest/scale-to-width-down/332?cb=20110513152209",
                         "https://www.youtube.com/watch?v=k64P4l2Wmeg","107")

backtofuture = media.Movie("Back to the Future", "Time travel by a school student",
                           "http://good-movie.ru/_pu/31/92926070.jpg",
                           "https://www.youtube.com/watch?v=qvsgGtivCgs","116")

schoolofrock = media.Movie("School of Rock","A story of sub music teacher",
                           "http://static.rogerebert.com/uploads/movie/movie_poster/school-of-rock-2003/large_cREN222Yw78zvSQ9bg17Y9QZS0c.jpg",
                           "https://www.youtube.com/watch?v=XCwy6lW5Ixc","108")

movies = [toystory,terminator,backtofuture,schoolofrock]

#print movies
open_movies_page(movies) # calling open_movies_page function of the Fresh_tomatoes module
#print media.Movie.__doc__

#print toystory.storyline
#print toystory.show_trailer()
#print toystory.show_poster()

#print media.Movie.VALID_RATINGS


