__author__ = 'eduar'

class Movie():
    """This class provides the minimal requirements to create instances of the type movie.

    It has as attributes the title of the movie, a storyline giving a brief of the movie itself,
    a image URL which links to the movie poster, and a youtube link for the movies's trailer.
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube