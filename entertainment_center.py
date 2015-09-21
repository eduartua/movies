__author__ = 'eduar'

import media
import fresh_tomatoes

# Each one below is an instance of a movie.

robocop = media.Movie("RoboCop", "A superhuman cyborg known as RoboCop.",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/5/50/Robocop_film.jpg/220px-Robocop_film.jpg",
                      "www.youtube.com/watch?v=zbCbwP6ibR4")

sixth_sense = media.Movie("The Six Sense", "A marine on an alien planet.",
                          "https://upload.wikimedia.org/wikipedia/en/6/66/The_sixth_sense.jpg",
                          "www.youtube.com/watch?v=VG9AGf66tXM")

starwars = media.Movie("Star Wars", "A battle in the outer space.",
                       "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5Vua_fg3Ut27HGrK5m2VNlJ-b4lqPI45FjymPZFuACg8SMEDb",
                       "https://www.youtube.com/watch?v=vZ734NWnAHA")

a_beautiful_mind = media.Movie("A Beautiful Mind", "The life of John Forbes Nash Jr.",
                               "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
                               "https://www.youtube.com/watch?v=WFJgUm7iOKw")

others = media.Movie("The Others", "The story of a ghost family",
                     "https://upload.wikimedia.org/wikipedia/en/4/4c/TheOthers.jpg",
                     "https://www.youtube.com/watch?v=0bMEGtUxajY")

silver_linings = media.Movie("Silver Linings Playbook","A couple of strangers with mental problems that fell in love.",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Silver_Linings_Playbook_Poster.jpg/220px-Silver_Linings_Playbook_Poster.jpg",
                             "www.youtube.com/watch?v=Lj5_FhLaaQQ")

movies = [robocop, sixth_sense, starwars, a_beautiful_mind, others, silver_linings]
fresh_tomatoes.open_movies_page(movies)