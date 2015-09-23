import media
import fresh_tomatoes

__author__ = 'eduar'

# The next code represents an instance named robocop which is built using
# the class movie from the module media.

robocop = media.Movie("RoboCop", "A superhuman cyborg known as RoboCop.",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/5/50/Robocop_film.jpg/220px-Robocop_film.jpg",  # noqa
                      "www.youtube.com/watch?v=zbCbwP6ibR4")

# The next code represents an instance named sixth_sense which is built using
# the class movie from the module media.

sixth_sense = media.Movie("The Six Sense", "A marine on an alien planet.",
                          "https://upload.wikimedia.org/wikipedia/en/6/66/The_sixth_sense.jpg",  # noqa
                          "www.youtube.com/watch?v=VG9AGf66tXM")

# The next code represents an instance named starwars which is built using
# the class movie from the module media.

starwars = media.Movie("Star Wars", "A battle in the outer space.",
                       "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5Vua_fg3Ut27HGrK5m2VNlJ-b4lqPI45FjymPZFuACg8SMEDb",  # noqa
                       "https://www.youtube.com/watch?v=vZ734NWnAHA")

# The next code represents an instance named a_beautiful_mind which is built
# using the class movie from the module media.

a_beautiful_mind = media.Movie("A Beautiful Mind", "The life of John Forbes Na\
                               sh Jr.",
                               "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",  # noqa
                               "https://www.youtube.com/watch?v=WFJgUm7iOKw")

# The next code represents an instance named others which is built
# using the class movie from the module media.

others = media.Movie("The Others", "The story of a ghost family",
                     "https://upload.wikimedia.org/wikipedia/en/4/4c/TheOthers.jpg",  # noqa
                     "https://www.youtube.com/watch?v=0bMEGtUxajY")

# The next code represents an instance named silver_linings which is built
# using the class movie from the module media.

silver_linings = media.Movie("Silver Linings Playbook", "A couple of strangers \
                             with mental problems that fell in love.",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Silver_Linings_Playbook_Poster.jpg/220px-Silver_Linings_Playbook_Poster.jpg",  # noqa
                             "www.youtube.com/watch?v=Lj5_FhLaaQQ")

# List that includes the whole instances required to build the web page, and it
# is going to be used by the fresh_tomatoes.py script.
movies = [robocop, sixth_sense, starwars, a_beautiful_mind, others,
          silver_linings]

# Calling the function open_movies_page that is stated within the
# fresh_tomatoes script.
fresh_tomatoes.open_movies_page(movies)