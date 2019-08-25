class Song:
    def __init__(self, title, artist, duration=0):

        self.title = title
        self.artist = artist
        self.duration = duration

help(Song.__init__)

class Album:

def __init__(self, name, year, artist=None):

    self.name = name
    self.year = year

    if artist is None:
        self.artist = artist("Various artists")
    else:
        self.artist = artist

class Artist:
    def __init__(self, name):

        self.name = name
        self.albums = []

    def add_album(self, album):

        self.albums.append(album)


def load_data():

    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)