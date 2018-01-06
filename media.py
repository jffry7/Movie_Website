#!/usr/bin/python
# coding=utf-8
import webbrowser


class Movie():
    """Creates a library of commands for reused functions when making movie list."""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """Form a class for creating movie site.

        Args:
        title -- Movie title
        storyline -- movie plot
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        # gets the video from youtube and play
