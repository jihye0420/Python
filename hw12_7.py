class Song:
    def __init__(self, title, artist, album, track_number):
        self.title = title
        self.artist = artist
        self.album = album
        self.track_number = track_number
        artist.add_song(self)

class Album:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
        self.tracks = []
        artist.add_album(self)

    def add_track(self, title, artist=None):
        if artist is None:
            artist = self.artist

        track_number = len(self.tracks)
        song = Song(title, artist, self, track_number)
        self.tracks.append(song)

class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []
        self.songs = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

lee = Artist("Lee's Band")
album = Album("첫 번째 앨범", lee, 2020)
album.add_track("첫 번째 노래")
album.add_track("두 번째 노래")

playlist = Playlist("애창곡")

for song in album.tracks:
    playlist.add_song(song)